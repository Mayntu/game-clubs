from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ServiceBase(BaseModel):
    id : UUID
    title : str
    description : Optional[str]
    icon_url : str

    class Config:
        orm_mode = True
        from_attributes = True


class CreateServiceRequest(BaseModel):
    title : str
    description : Optional[str]
    icon_url : str