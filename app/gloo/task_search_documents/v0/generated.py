
import typing
from ...types import SearchOutputModel__Description, SearchOutputModel__OutputTemplateVars, SearchInputModel__InputTemplateVars

class search_documents__Description(typing.TypedDict):
    SearchOutput: SearchOutputModel__Description

class search_documents__TemplateVars:
    in_SearchInput: SearchInputModel__InputTemplateVars = SearchInputModel__InputTemplateVars()
    out_SearchOutput: SearchOutputModel__OutputTemplateVars = SearchOutputModel__OutputTemplateVars()


VARS = search_documents__TemplateVars()

__all__ = ["search_documents__Description", "VARS"]
