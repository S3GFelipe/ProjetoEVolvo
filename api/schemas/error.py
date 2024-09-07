from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Padroniza como uma mensagem de erro será apresentada
    """
    mesage: str
