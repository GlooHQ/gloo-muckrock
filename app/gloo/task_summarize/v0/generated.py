import typing
from ...types import SummarizeInputModel__InputVars
from ...types import SummarizeOutputModel__Definition, SummarizeOutputModel__OutputVars

class summarize__Definition(typing.TypedDict):
    SummarizeOutput: SummarizeOutputModel__Definition

class summarize__Vars:
    input: SummarizeInputModel__InputVars = SummarizeInputModel__InputVars()
    output: SummarizeOutputModel__OutputVars = SummarizeOutputModel__OutputVars()


VARS = summarize__Vars()

__all__ = ["summarize__Definition", "VARS"]