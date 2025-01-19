from fastapi.exceptions import HTTPException
from uuid import UUID

from src.dto.zone import (
    ZoneBase,
    CreateZoneRequest
)
from src.models.models import Zone

async def create_zone(request : CreateZoneRequest) -> ZoneBase:
    try:
        zone : Zone = await Zone.create(
            title=request.title,
            description=request.description,
            computers_count=request.computers_count,
            club_id=request.club_id,
            computer_config_id=request.computer_config_id
        )
    except:
        raise HTTPException(status_code=400, detail="not valid zone parameters request")

    return ZoneBase.from_orm(zone)

async def find_zone(zone_id : str) -> ZoneBase:
    try:
        zone : Zone = await Zone.get(id=UUID(zone_id))
    except:
        raise HTTPException(status_code=404, detail="not found zone")
    
    return ZoneBase.model_validate(zone)