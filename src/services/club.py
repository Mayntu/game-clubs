from fastapi.exceptions import HTTPException
from uuid import UUID

from src.dto.club import (
    CreateClubRequest,
    UpdateClubRequest,
    ClubBase
)
from src.models.models import Club

import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def create_club(request : CreateClubRequest) -> ClubBase:
    try:
        club : Club = await Club.create(
            title=request.title,
            description=request.description,
            address=request.address,
            coord_lat=request.coord_lat,
            coord_lon=request.coord_lon,
            city=request.city
        )
    except:
        raise HTTPException(status_code=400, detail="not valid club parameters request")

    return ClubBase.model_validate(club)


async def find_club(club_id : str) -> ClubBase:
    club : Club = await get_club(club_id=club_id)
    
    return ClubBase.model_validate(club)

async def find_clubs_by_city(city : str) -> list[ClubBase]:
    clubs : list[Club] = await Club.filter(city=city)
    
    return [ClubBase.model_validate(club) for club in clubs]


async def update_club(club_id : str, request : UpdateClubRequest) -> ClubBase:
    club : Club = await get_club(club_id=club_id)
    
    try:
        club.title = request.title if request.title else club.title
        club.description = request.description if request.description else club.description
        club.address = request.address if request.address else club.address

        await club.save()
        return ClubBase.model_validate(club)
    except Exception as e:
        log.error(f"failed to update_club : {e}")
        raise HTTPException(status_code = 400, detail = "not valid club parameters")


async def delete_club(club_id : str) -> None:
    club : Club = await get_club(club_id=club_id)
    
    try:
        await club.delete()
    except Exception as e:
        log.error(f"failed to delete club : {e}")
        raise HTTPException(status_code=400, detail="failed to delete club")



async def get_club(club_id : str) -> Club:
    try:
        club : Club = await Club.get(id=UUID(club_id))
    except:
        raise HTTPException(status_code=404, detail="not found club")
    
    return club
