from fastapi.exceptions import HTTPException
from uuid import UUID

from src.dto.club import (
    CreateClubRequest,
    ClubBase
)
from src.models.models import Club

async def create_club(request : CreateClubRequest) -> ClubBase:
    try:
        club : Club = await Club.create(
            title=request.title,
            description=request.description,
            address=request.address
        )
    except:
        raise HTTPException(status_code=400, detail="not valid club parameters request")

    return ClubBase.from_orm(club)


async def find_club(club_id : str) -> ClubBase:
    try:
        club : Club = await Club.get(id=UUID(club_id))
    except:
        raise HTTPException(status_code=404, detail="not found club")
    
    return ClubBase.model_validate(club)