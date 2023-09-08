import logging
from typing import List, Callable, Awaitable, Any, Dict

from enum import Enum

import os
import pandas as pd
from collections import defaultdict
from generated.functions import ExtractRequestData, Summarize
from generated.custom_types import RecordsStatus, RequestStatus
from pydantic import BaseModel
import json
import os
from generated.custom_types import FoiaTestCasePayload, FOIARequestData


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


def map_status(status: RequestStatus, recordsStatus: RecordsStatus):
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
            RequestStatus.PENDING_MORE_DOCS,
            RecordsStatus.MORE_RECORDS_PENDING,
        ),
    }
    status, records_status = status_mapping.get(
        mrStatus, (RequestStatus.INDETERMINATE, RecordsStatus.NOT_APPLICABLE)
    )
    return ExpectedOutput(status=status, recordsStatus=records_status)


async def process_request(input: str) -> FOIARequestData:
    summarize_response = await Summarize("v1", input)

    extractedData = await ExtractRequestData(
        "v1",
        summarize_response,
    )

    return extractedData


# This function is called by the Gloo ProcessRequestTestWrapper function in process-request-test-fn.gloo
# This function just takes more test metadata as its input, and then calls the "real" production function
# "process_request" above.
# We do this right now so Gloo publishes all of the FoiaTestCasePayload to the dashboard when this
# function is called, to be able to view associated metadata with each test case.
# The need to declare the .gloo function may be removed in favor of a simpler
# @gloo_test annotation.
async def process_request_test(test_case: FoiaTestCasePayload) -> FOIARequestData:
    file_text = ""
    if test_case.file_text is not None and test_case.file_text != "None":
        file_text = f"Attached Correspondence:\n{test_case.file_text}"

    request_text = f"{test_case.communication}\n{file_text}"
    extracted_data = await process_request(request_text)

    expected_output = expected_gloo_statuses(MRStatus(test_case.status))
    request_status = extracted_data.requestStatus
    assert request_status == expected_output.status

    if request_status == RequestStatus.REQUEST_COMPLETED:
        assert extracted_data.recordsStatus == expected_output.recordsStatus
    return extracted_data
