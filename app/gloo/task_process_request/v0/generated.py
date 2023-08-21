import typing
from ...types import ClassifyRequestInputModel__InputVars
from ...types import ClassifyRequestOutputModel__Definition, ClassifyRequestOutputModel__OutputVars
from ...types import StatusModel__Definition, StatusModel__OutputVars

class process_request__Definition(typing.TypedDict):
    ClassifyRequestOutput: ClassifyRequestOutputModel__Definition
    Status: StatusModel__Definition

class process_request__Vars:
    input: ClassifyRequestInputModel__InputVars = ClassifyRequestInputModel__InputVars()
    output: ClassifyRequestOutputModel__OutputVars = ClassifyRequestOutputModel__OutputVars()
    out_Status: StatusModel__OutputVars = StatusModel__OutputVars()


VARS = process_request__Vars()

__all__ = ["process_request__Definition", "VARS"]