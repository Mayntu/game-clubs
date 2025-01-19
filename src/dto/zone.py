from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ZoneBase(BaseModel):
    id : UUID
    title : str
    description : Optional[str]
    computers_count : int
    club_id : UUID
    computer_config_id : UUID

    class Config:
        orm_mode = True
        from_attributes=True


class CreateZoneRequest(BaseModel):
    title : str
    description : Optional[str]
    computers_count : int
    club_id : UUID
    computer_config_id : UUID