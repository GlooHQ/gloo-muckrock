import logging
from typing import List, Callable, Awaitable, Any, Dict

from gloo_py.testing import with_suite, GlooTestCaseBase, GlooTestDataset
from gloo_py import init_gloo, GlooLogger
from .task import run_process_request_v1_async
from ...types import ClassifyRequestInputModel

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
max_count = 40
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


def map_status(status):
    status_mapping = {
        "no_docs": "NO_DOCS",
        "processed": "PROCESSED",
        "payment": "PAYMENT",
        "done": "DONE",
        "fix": "FIX",
        "abandoned": "INDETERMINATE",
        "appealing": "INDETERMINATE",
        "rejected": "REJECTED",
        "partial": "PARTIAL",
    }
    return status_mapping.get(status, "INDETERMINATE")


# Gloo tester will automatically run and publish test results for you if you init_gloo(..) here or
# anywhere in the code call path.
@with_suite(suites)
async def test_process_request(
    test_case: Case, logger: Callable[[Any], Awaitable[None]]
):
    print(colored(f"Running test case {test_case['name']}", "green"))

    request_text = f'```{test_case["communication"]}```\nContains attachments? {"Yes" if test_case["file_text"] != "" or test_case["file_text"] is not None else "No"}'

    res = await run_process_request_v1_async(
        ClassifyRequestInputModel(
            request=request_text,
        )
    )
    assert res.classification.status.value == map_status(test_case["status"])
