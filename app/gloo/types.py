import typing
from pydantic import BaseModel
from enum import StrEnum
from gloo_py.llm_task_interface.vars_manager import FieldDefinition, FieldVars

# ===============================================
# Types from yaml
# ===============================================


class SummarizeInputModel(BaseModel):
    text: str


class SummarizeOutputModel(BaseModel):
    summary: str


class ClassifyRequestInputModel(BaseModel):
    request: str


class StatusModel(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    FIX_REQUIRED = "FIX_REQUIRED"
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    REQUEST_REJECTED = "REQUEST_REJECTED"
    REQUEST_COMPLETED = "REQUEST_COMPLETED"
    PENDING_MORE_DOCS = "PENDING_MORE_DOCS"
    INDETERMINATE = "INDETERMINATE"


class RecordsStatusModel(StrEnum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    RECORDS_FOUND = "RECORDS_FOUND"
    NO_RECORDS_FOUND = "NO_RECORDS_FOUND"
    MORE_RECORDS_PENDING = "MORE_RECORDS_PENDING"


class ClassificationModel(BaseModel):
    reasoning: str
    requestStatus: StatusModel


class ClassifyRequestOutputModel(BaseModel):
    trackingNumber: str
    dateEstimate: str
    price: int
    recordsStatus: RecordsStatusModel
    requestStatus: ClassificationModel


# ===============================================
# Below are helper types for better auto complete
# ===============================================


class SummarizeInputModel__Definition(typing.TypedDict):
    text: FieldDefinition


class SummarizeInputModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.text = f"{{{prefix}text}}"
        self.__val = f"{{{prefix}SummarizeInput.val}}"

    def __str__(self):
        return self.__val


class SummarizeInputModel__OutputVars:
    def __init__(self):
        self.text = FieldVars(name="SummarizeInput.text")

        self.json = "{" + "SummarizeInput.json}"

    def __str__(self):
        return self.json


class SummarizeOutputModel__Definition(typing.TypedDict):
    summary: FieldDefinition


class SummarizeOutputModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.summary = f"{{{prefix}summary}}"
        self.__val = f"{{{prefix}SummarizeOutput.val}}"

    def __str__(self):
        return self.__val


class SummarizeOutputModel__OutputVars:
    def __init__(self):
        self.summary = FieldVars(name="SummarizeOutput.summary")

        self.json = "{" + "SummarizeOutput.json}"

    def __str__(self):
        return self.json


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
    IN_PROGRESS: FieldDefinition
    FIX_REQUIRED: FieldDefinition
    PAYMENT_REQUIRED: FieldDefinition
    REQUEST_REJECTED: FieldDefinition
    REQUEST_COMPLETED: FieldDefinition
    PENDING_MORE_DOCS: FieldDefinition
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


class RecordsStatusCases__Definition(typing.TypedDict, total=False):
    NOT_APPLICABLE: FieldDefinition
    RECORDS_FOUND: FieldDefinition
    NO_RECORDS_FOUND: FieldDefinition
    MORE_RECORDS_PENDING: FieldDefinition


class RecordsStatusModel__Definition(FieldDefinition):
    case_name_formatter: typing.Callable[[str], str]
    case_formatter: typing.Callable[[str, str], str]
    cases: RecordsStatusCases__Definition


class RecordsStatusModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.val = f"{{{prefix}RecordsStatus.val}}"

    def __str__(self):
        return self.val


class RecordsStatusModel__OutputVars(FieldVars):
    def __init__(self):
        super().__init__(name="RecordsStatus")
        self.cases = "{" + "RecordsStatus.cases}"
        self.case_names = "{" + "RecordsStatus.case_names}"

    def __str__(self):
        return self.cases


class ClassificationModel__Definition(typing.TypedDict):
    reasoning: FieldDefinition
    requestStatus: StatusModel__Definition


class ClassificationModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.reasoning = f"{{{prefix}reasoning}}"
        self.requestStatus = StatusModel__InputVars(prefix=f"{prefix}requestStatus.")
        self.__val = f"{{{prefix}Classification.val}}"

    def __str__(self):
        return self.__val


class ClassificationModel__OutputVars:
    def __init__(self):
        self.reasoning = FieldVars(name="Classification.reasoning")
        self.requestStatus = FieldVars(name="Classification.requestStatus")

        self.json = "{" + "Classification.json}"

    def __str__(self):
        return self.json


class ClassifyRequestOutputModel__Definition(typing.TypedDict):
    trackingNumber: FieldDefinition
    dateEstimate: FieldDefinition
    price: FieldDefinition
    recordsStatus: RecordsStatusModel__Definition
    requestStatus: FieldDefinition


class ClassifyRequestOutputModel__InputVars:
    def __init__(self, prefix: str = ""):
        self.trackingNumber = f"{{{prefix}trackingNumber}}"
        self.dateEstimate = f"{{{prefix}dateEstimate}}"
        self.price = f"{{{prefix}price}}"
        self.recordsStatus = RecordsStatusModel__InputVars(
            prefix=f"{prefix}recordsStatus."
        )
        self.requestStatus = ClassificationModel__InputVars(
            prefix=f"{prefix}requestStatus."
        )
        self.__val = f"{{{prefix}ClassifyRequestOutput.val}}"

    def __str__(self):
        return self.__val


class ClassifyRequestOutputModel__OutputVars:
    def __init__(self):
        self.trackingNumber = FieldVars(name="ClassifyRequestOutput.trackingNumber")
        self.dateEstimate = FieldVars(name="ClassifyRequestOutput.dateEstimate")
        self.price = FieldVars(name="ClassifyRequestOutput.price")
        self.recordsStatus = FieldVars(name="ClassifyRequestOutput.recordsStatus")
        self.requestStatus = FieldVars(name="ClassifyRequestOutput.requestStatus")

        self.json = "{" + "ClassifyRequestOutput.json}"

    def __str__(self):
        return self.json
