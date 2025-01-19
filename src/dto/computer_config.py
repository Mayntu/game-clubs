from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ComputerConfigBase(BaseModel):
    id : UUID
    cpu : Optional[str]
    gpu : Optional[str]
    ram : Optional[str]
    keyboard : Optional[str]
    mouse : Optional[str]
    headset : Optional[str]
    armchair : Optional[str]
    monitor : Optional[str]
    internet : Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True


class CreateComputerConfigRequest(BaseModel):
    cpu : Optional[str]
    gpu : Optional[str]
    ram : Optional[str]
    keyboard : Optional[str]
    mouse : Optional[str]
    headset : Optional[str]
    armchair : Optional[str]
    monitor : Optional[str]
    internet : Optional[str]
