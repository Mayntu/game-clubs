from fastapi import APIRouter

from src.dto.club import ClubBase, CreateClubRequest
from src.services.club import create_club, find_club

views : APIRouter = APIRouter()


@views.post("", response_model=ClubBase, status_code=201)
async def post_club(request : CreateClubRequest) -> ClubBase:
    club = await create_club(request=request)
    return club

@views.get("/{club_id}", response_model=ClubBase, status_code=200)
async def get_club(club_id : str) -> ClubBase:
    return await find_club(club_id=club_id)