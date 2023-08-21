import logging
from typing import List, Callable, Awaitable, Any

from gloo_py.testing import with_suite, GlooTestCaseBase, GlooTestDataset
from gloo_py import init_gloo, GlooLogger
from .task import run_process_request_v0_async
from ...types import ClassifyRequestInputModel

logging.basicConfig(level=logging.INFO)
from termcolor import colored


class Case(GlooTestCaseBase):
    test_input: str
    # You can also add an expected result that you can use
    # in the test function.
    # expected_result: str


# You can create as many datasets as you want.
suite = GlooTestDataset[Case](
    name="test-group1",
    test_cases=[
        Case(
            name="test-input-name1",
            test_input="custom-test-input",
        ),
        # Case(
        #     name="test-input-name2",
        #     test_input="custom-test-input2",
        # ),
    ],
)

# To see your test results and logs posted online at https://app.trygloo.com, initialize
#  this with your projectID and API key from the dashboard.:
# init_gloo(gloo_api_key=, gloo_project_id="", log_level="verbose")


# Gloo tester will automatically run and publish test results for you if you init_gloo(..) here or
# anywhere in the code call path.
# @with_suite([suite])
# async def test_process_request(
#     test_case: Case, logger: Callable[[Any], Awaitable[None]]
# ):
#     print(colored(f"Running test case {test_case['name']}", "green"))
#     res = await run_process_request_v0_async(
#         ClassifyRequestInputModel(request=test_case["test_input"])
#     )
