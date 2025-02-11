from fastapi import APIRouter
from typing import List

from src.dto.club import ClubBase, CreateClubRequest, UpdateClubRequest
from src.services.club import create_club, find_club, update_club, delete_club, find_clubs_by_city

views : APIRouter = APIRouter()


@views.post("", response_model=ClubBase, status_code=201)
async def post_club(request : CreateClubRequest) -> ClubBase:
    club = await create_club(request=request)
    return club

@views.get("/{club_id}", response_model=ClubBase, status_code=200)
async def get_club(club_id : str) -> ClubBase:
    return await find_club(club_id=club_id)

@views.get("/city/{city}", response_model=List[ClubBase], status_code=200)
async def get_clubs_by_city(city : str) -> List[ClubBase]:
    return await find_clubs_by_city(city=city)

@views.patch("/{club_id}", response_model=ClubBase, status_code=200)
async def patch_club(club_id : str, request : UpdateClubRequest) -> ClubBase:
    return await update_club(club_id=club_id, request=request)

@views.delete("/{club_id}", status_code=204)
async def delete_club(club_id : str) -> None:
    await delete_club(club_id=club_id)
    return None
