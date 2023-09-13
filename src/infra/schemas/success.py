from pydantic import BaseModel


class SuccessSchema(BaseModel):
    """ Define como uma mensagem de sucesso será representada
    """
    id: str
    message: str
