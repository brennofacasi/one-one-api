from pydantic import BaseModel


class SuccessSchemaWithId(BaseModel):
    """ Define como uma mensagem de sucesso será representada
    """
    id: str
    message: str


class SuccessSchema(BaseModel):
    """ Define como uma mensagem de sucesso será representada
    """
    message: str
