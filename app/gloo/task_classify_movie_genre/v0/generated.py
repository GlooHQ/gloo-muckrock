
import typing
from ...types import ClassifyMovieOutputModel__Description, ClassifyMovieOutputModel__OutputTemplateVars, GenreModel__Description, GenreModel__OutputTemplateVars, ClassifyMovieInputModel__InputTemplateVars

class classify_movie_genre__Description(typing.TypedDict):
    ClassifyMovieOutput: ClassifyMovieOutputModel__Description
    Genre: GenreModel__Description

class classify_movie_genre__TemplateVars:
    in_ClassifyMovieInput: ClassifyMovieInputModel__InputTemplateVars = ClassifyMovieInputModel__InputTemplateVars()
    out_ClassifyMovieOutput: ClassifyMovieOutputModel__OutputTemplateVars = ClassifyMovieOutputModel__OutputTemplateVars()
    out_Genre: GenreModel__OutputTemplateVars = GenreModel__OutputTemplateVars()


VARS = classify_movie_genre__TemplateVars()

__all__ = ["classify_movie_genre__Description", "VARS"]
