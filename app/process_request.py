# Standard Library
import json
import logging
import os
from collections import defaultdict
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List

# Third Party
import pandas as pd
import tiktoken
from gloo_py import trace, update_trace_tags
from pydantic import BaseModel

from ..generated.custom_types import (
    FOIARequestData,
    FoiaTestCasePayload,
    RecordsStatus,
    RequestStatus,
)
from ..generated.functions import ExtractRequestData, Summarize


class MRStatus(Enum):
    NO_DOCS = "no_docs"
    PROCESSED = "processed"
    PAYMENT = "payment"
    DONE = "done"
    FIX = "fix"
    ABANDONED = "abandoned"
    APPEALING = "appealing"
    REJECTED = "rejected"
    PARTIAL = "partial"
    INDETERMINATE = "indeterminate"


def map_status_(status: RequestStatus, recordsStatus: RecordsStatus):
    status_mapping = {
        MRStatus.NO_DOCS.value: "",
        MRStatus.PROCESSED.value: "IN_PROGRESS",
        MRStatus.PAYMENT.value: "PAYMENT",
        MRStatus.DONE.value: "DONE",
        MRStatus.FIX.value: "FIX",
        MRStatus.ABANDONED.value: "INDETERMINATE",
        MRStatus.APPEALING.value: "INDETERMINATE",
        MRStatus.REJECTED.value: "REJECTED",
        MRStatus.PARTIAL.value: "PARTIAL",
    }
    return status_mapping.get(status, "INDETERMINATE")


def map_status(data: FOIARequestData) -> MRStatus:

    both = (data.requestStatus, data.recordsStatus)
    req = data.requestStatus

    if both == (RequestStatus.REQUEST_COMPLETED, RecordsStatus.NO_RECORDS_FOUND):
        return MRStatus.NO_DOCS
    elif both == (RequestStatus.REQUEST_COMPLETED, RecordsStatus.RECORDS_FOUND):
        return MRStatus.DONE
    elif both == (RequestStatus.IN_PROGRESS, RecordsStatus.MORE_RECORDS_PENDING):
        return MRStatus.PARTIAL
    elif both == (RequestStatus.IN_PROGRESS, RecordsStatus.RECORDS_FOUND):
        return MRStatus.PARTIAL
    elif req == RequestStatus.IN_PROGRESS:
        return MRStatus.PROCESSED
    elif req == RequestStatus.PAYMENT_REQUIRED:
        return MRStatus.PAYMENT
    elif req == RequestStatus.FIX_REQUIRED:
        return MRStatus.FIX
    elif req == RequestStatus.REQUEST_REJECTED:
        return MRStatus.REJECTED
    else:
        return MRStatus.INDETERMINATE


class ExpectedOutput(BaseModel):
    status: RequestStatus
    recordsStatus: RecordsStatus


def expected_gloo_statuses(mrStatus: MRStatus) -> ExpectedOutput:
    status_mapping = {
        MRStatus.NO_DOCS: (
            RequestStatus.REQUEST_COMPLETED,
            RecordsStatus.NO_RECORDS_FOUND,
        ),
        MRStatus.PROCESSED: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.PAYMENT: (
            RequestStatus.PAYMENT_REQUIRED,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.DONE: (
            RequestStatus.REQUEST_COMPLETED,
            RecordsStatus.RECORDS_FOUND,
        ),
        MRStatus.FIX: (RequestStatus.FIX_REQUIRED, RecordsStatus.NOT_APPLICABLE),
        MRStatus.ABANDONED: (
            RequestStatus.INDETERMINATE,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.APPEALING: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.REJECTED: (
            RequestStatus.REQUEST_REJECTED,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.PARTIAL: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.MORE_RECORDS_PENDING,
        ),
    }
    status, records_status = status_mapping.get(
        mrStatus, (RequestStatus.INDETERMINATE, RecordsStatus.NOT_APPLICABLE)
    )
    return ExpectedOutput(status=status, recordsStatus=records_status)


enc = tiktoken.encoding_for_model("gpt-4")


@trace()
async def process_request(request_text: str, file_text: str, **tags) -> (FOIARequestData, str):

    if tags:
        update_trace_tags(**tags)

    if file_text:
        file_text = f"Attached Correspondence:\n{file_text}"
        request_text = f"{request_text}\n{file_text}"

    tokens = enc.encode(request_text)
    ellipsis_tokens = enc.encode("...")
    max_tokens = 2000
    if len(tokens) > max_tokens:
        tokens = tokens[: max_tokens - len(ellipsis_tokens)] + ellipsis_tokens
    request_text = enc.decode(tokens)

    extractedData = await ExtractRequestData(
        "v1",
        request_text,
    )
    status = map_status(extractedData)
    update_trace_tags(
        status=status.value,
        has_tracking=str(extractedData.trackingNumber is not None),
        has_date=str(extractedData.dateEstimate is not None),
    )

    return (extractedData, status.value)


# This function is called by the Gloo ProcessRequestTestWrapper function in process-request-test-fn.gloo
# This function just takes more test metadata as its input, and then calls the "real" production function
# "process_request" above.
# We do this right now so Gloo publishes all of the FoiaTestCasePayload to the dashboard when this
# function is called, to be able to view associated metadata with each test case.
# The need to declare the .gloo function may be removed in favor of a simpler
# @gloo_test annotation.
async def process_request_test(test_case: FoiaTestCasePayload) -> (FOIARequestData, str):

    extracted_data, status = await process_request(test_case.communication, test_case.file_text)

    assert status == test_case.status

    if test_case.price:
        assert extracted_data.price == test_case.price

    return extracted_data, status


async def process_request_metadata_test(
    test_case: FoiaTestCasePayload,
) -> FOIARequestData:

    extracted_data, _status = await process_request(test_case.communication, test_case.file_text)

    if test_case.tracking_number:
        assert extracted_data.trackingNumber == test_case.tracking_number

    if test_case.date_estimate:
        assert extracted_data.dateEstimate == test_case.date_estimate

    return extracted_data
