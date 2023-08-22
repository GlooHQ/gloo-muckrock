import typing
from pydantic import BaseModel
from enum import StrEnum
from gloo_py.llm_task_interface.vars_manager import FieldDefinition, FieldVars

# ===============================================
# Types from yaml
# ===============================================


class ClassifyRequestInputModel(BaseModel):
    request: str


class StatusModel(StrEnum):
    PROCESSED = "PROCESSED"
    FIX = "FIX"
    PAYMENT = "PAYMENT"
    REJECTED = "REJECTED"
    NO_DOCS = "NO_DOCS"
    DONE = "DONE"
    PARTIAL = "PARTIAL"
    INDETERMINATE = "INDETERMINATE"


class ClassificationModel(BaseModel):
    clues: str
    reasoning: str
    status: StatusModel


class ClassifyRequestOutputModel(BaseModel):
    trackingNumber: str
    dateEstimate: str
    price: int
    classification: ClassificationModel


# ===============================================
# Below are helper types for better auto complete
# ===============================================


class ClassifyRequestInputModel__Definition(typing.TypedDict):
    request: FieldDefinition


class ClassifyRequestInputModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.request = f"{{{prefix}request}}"
        self.__val = f"{{{prefix}ClassifyRequestInput.val}}"

    def __str__(self):
        return self.__val


class ClassifyRequestInputModel__OutputVars:
    def __init__(self):
        self.request = FieldVars(name="ClassifyRequestInput.request")

        self.json = "{" + "ClassifyRequestInput.json}"

    def __str__(self):
        return self.json


class StatusCases__Definition(typing.TypedDict, total=False):
    PROCESSED: FieldDefinition
    FIX: FieldDefinition
    PAYMENT: FieldDefinition
    REJECTED: FieldDefinition
    NO_DOCS: FieldDefinition
    DONE: FieldDefinition
    PARTIAL: FieldDefinition
    INDETERMINATE: FieldDefinition


class StatusModel__Definition(FieldDefinition):
    case_name_formatter: typing.Callable[[str], str]
    case_formatter: typing.Callable[[str, str], str]
    cases: StatusCases__Definition


class StatusModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.val = f"{{{prefix}Status.val}}"

    def __str__(self):
        return self.val


class StatusModel__OutputVars(FieldVars):
    def __init__(self):
        super().__init__(name="Status")
        self.cases = "{" + "Status.cases}"
        self.case_names = "{" + "Status.case_names}"

    def __str__(self):
        return self.cases


class ClassificationModel__Definition(typing.TypedDict):
    clues: FieldDefinition
    reasoning: FieldDefinition
    status: StatusModel__Definition


class ClassificationModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.clues = f"{{{prefix}clues}}"
        self.reasoning = f"{{{prefix}reasoning}}"
        self.status = StatusModel__InputVars(prefix=f"{prefix}status.")
        self.__val = f"{{{prefix}Classification.val}}"

    def __str__(self):
        return self.__val


class ClassificationModel__OutputVars:
    def __init__(self):
        self.clues = FieldVars(name="Classification.clues")
        self.reasoning = FieldVars(name="Classification.reasoning")
        self.status = FieldVars(name="Classification.status")

        self.json = "{" + "Classification.json}"

    def __str__(self):
        return self.json


class ClassifyRequestOutputModel__Definition(typing.TypedDict):
    trackingNumber: FieldDefinition
    dateEstimate: FieldDefinition
    price: FieldDefinition
    classification: FieldDefinition


class ClassifyRequestOutputModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.trackingNumber = f"{{{prefix}trackingNumber}}"
        self.dateEstimate = f"{{{prefix}dateEstimate}}"
        self.price = f"{{{prefix}price}}"
        self.classification = ClassificationModel__InputVars(
            prefix=f"{prefix}classification."
        )
        self.__val = f"{{{prefix}ClassifyRequestOutput.val}}"

    def __str__(self):
        return self.__val


class ClassifyRequestOutputModel__OutputVars:
    def __init__(self):
        self.trackingNumber = FieldVars(name="ClassifyRequestOutput.trackingNumber")
        self.dateEstimate = FieldVars(name="ClassifyRequestOutput.dateEstimate")
        self.price = FieldVars(name="ClassifyRequestOutput.price")
        self.classification = FieldVars(name="ClassifyRequestOutput.classification")

        self.json = "{" + "ClassifyRequestOutput.json}"

    def __str__(self):
        return self.json
