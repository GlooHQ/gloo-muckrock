import logging
from typing import List, Callable, Awaitable, Any, Dict

from gloo_py.testing import with_suite, GlooTestCaseBase, GlooTestDataset
from gloo_py import init_gloo, GlooLogger
from pydantic import BaseModel
from .task import run_process_request_v1_async
from ...types import (
    ClassifyRequestInputModel,
    SummarizeInputModel,
    RecordsStatusModel,
    StatusModel,
)
from ...task_summarize import run_summarize_async
from enum import Enum

from termcolor import colored
import os
import pandas as pd
from collections import defaultdict

import json
import os

logging.basicConfig(level=logging.INFO)


class Case(GlooTestCaseBase):
    tid: int
    cid: int
    username: str
    communication: str
    file_text: str
    status: str
    tracking_number: str | None
    date_estimate: str | None
    price: int | None
    # You can also add an expected result that you can use
    # in the test function.
    # expected_result: str


print(os.getcwd())


with open("data/data.json", "r") as f:
    data = json.load(f)

test_cases: List[Case] = []
max_count = 70
for obj in data:
    obj["name"] = str(obj["tid"])
    # Replace all nans with None
    for k, v in obj.items():
        if isinstance(v, float) and pd.isna(v):
            obj[k] = None

    test_cases.append(Case(**obj))
    if len(test_cases) >= max_count:
        break


status_groups: Dict[str, List[Case]] = defaultdict(list)
for case in test_cases:
    status_groups[case["status"]].append(case)

suites: List[GlooTestDataset[Case]] = []
for status, cases in status_groups.items():
    if status in ["appealing", "abandoned"]:
        continue

    suite = GlooTestDataset[Case](
        name=f"status-{status}",
        test_cases=cases,
    )
    suites.append(suite)


# To see your test results and logs posted online at https://app.trygloo.com, initialize
#  this with your projectID and API key from the dashboard.:
init_gloo(
    gloo_project_id=os.environ.get("GLOO_PROJECT_ID", ""),
    gloo_api_key=os.environ.get(
        "GLOO_API_KEY",
        "",
    ),
    gloo_service=os.environ.get("GLOO_SERVICE", "https://app.trygloo.com/api"),
    openai_api_key=os.environ.get("OPENAI_KEY"),
    log_level="info",
)


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


def map_status(status: StatusModel, recordsStatus: RecordsStatusModel):
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
    status: StatusModel
    recordsStatus: RecordsStatusModel


def expected_gloo_statuses(mrStatus: MRStatus) -> ExpectedOutput:
    status_mapping = {
        MRStatus.NO_DOCS: (
            StatusModel.REQUEST_COMPLETED,
            RecordsStatusModel.NO_RECORDS_FOUND,
        ),
        MRStatus.PROCESSED: (
            StatusModel.IN_PROGRESS,
            RecordsStatusModel.NOT_APPLICABLE,
        ),
        MRStatus.PAYMENT: (
            StatusModel.PAYMENT_REQUIRED,
            RecordsStatusModel.NOT_APPLICABLE,
        ),
        MRStatus.DONE: (
            StatusModel.REQUEST_COMPLETED,
            RecordsStatusModel.RECORDS_FOUND,
        ),
        MRStatus.FIX: (StatusModel.FIX_REQUIRED, RecordsStatusModel.NOT_APPLICABLE),
        MRStatus.ABANDONED: (
            StatusModel.INDETERMINATE,
            RecordsStatusModel.NOT_APPLICABLE,
        ),
        MRStatus.APPEALING: (
            StatusModel.IN_PROGRESS,
            RecordsStatusModel.NOT_APPLICABLE,
        ),
        MRStatus.REJECTED: (
            StatusModel.REQUEST_REJECTED,
            RecordsStatusModel.NOT_APPLICABLE,
        ),
        MRStatus.PARTIAL: (
            StatusModel.PENDING_MORE_DOCS,
            RecordsStatusModel.MORE_RECORDS_PENDING,
        ),
    }
    status, records_status = status_mapping.get(
        mrStatus, (StatusModel.INDETERMINATE, RecordsStatusModel.NOT_APPLICABLE)
    )
    return ExpectedOutput(status=status, recordsStatus=records_status)


# Gloo tester will automatically run and publish test results for you if you init_gloo(..) here or
# anywhere in the code call path.
@with_suite(suites)
async def test_process_request(
    test_case: Case, logger: Callable[[Any], Awaitable[None]]
):
    print(colored(f"Running test case {test_case['name']}", "green"))

    file_text = ""
    if test_case["file_text"] is not None:
        file_text = f"Attached Correspondence:\n{test_case['file_text']}"

    request_text = f'{test_case["communication"]}\n{file_text}'
    summarize_response = await run_summarize_async(
        SummarizeInputModel(text=request_text)
    )
    res = await run_process_request_v1_async(
        ClassifyRequestInputModel(
            request=summarize_response.summary,
        )
    )

    expected_output = expected_gloo_statuses(MRStatus(test_case["status"]))
    request_status = res.requestStatus.requestStatus
    assert request_status == expected_output.status

    if request_status == StatusModel.REQUEST_COMPLETED:
        assert res.recordsStatus == expected_output.recordsStatus
