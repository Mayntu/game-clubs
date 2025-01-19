from fastapi import APIRouter

from src.dto.zone import ZoneBase, CreateZoneRequest
from src.services.zone import create_zone, find_zone

views : APIRouter = APIRouter()

@views.post("", response_model=ZoneBase, status_code=201)
async def post_zone(request : CreateZoneRequest) -> ZoneBase:
    zone : ZoneBase = await create_zone(request=request)
    return zone

@views.get("/{zone_id}", response_model=ZoneBase, status_code=200)
async def get_zone(zone_id : str) -> ZoneBase:
    zone : ZoneBase = await find_zone(zone_id=zone_id)
    return zone