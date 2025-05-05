from pydantic import BaseModel

class ProductUpdate(BaseModel):
    name: str