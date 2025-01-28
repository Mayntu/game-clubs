from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class ClubBase(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    rating: Optional[float]
    address: Optional[str]
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    is_deleted: bool

    class Config:
        orm_mode = True
        from_attributes=True


class CreateClubRequest(BaseModel):
    title : str
    description : Optional[str]
    address : str


class UpdateClubRequest(BaseModel):
    title : Optional[str]
    description : Optional[str]
    address : Optional[str]