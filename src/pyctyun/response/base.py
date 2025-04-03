from pydantic import BaseModel, Field


class BaseResponse(BaseModel):

    status_code: int = Field(alias='statusCode')
    message: str
    description: str
    error_code: str = Field(alias='errorCode')
