from fastapi.exceptions import HTTPException
from uuid import UUID

from src.dto.service import (
    ServiceBase,
    CreateServiceRequest
)
from src.models.models import Service


import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

async def create_service(request : CreateServiceRequest) -> ServiceBase:
    try:
        service : Service = await Service.create(
            title=request.title,
            description=request.description,
            icon_url=request.icon_url
        )
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=400, detail="not valid service parameters request")

    return ServiceBase.from_orm(service)

async def find_service(service_id : str) -> ServiceBase:
    try:
        service : Service = await Service.get(id=UUID(service_id))
    except:
        raise HTTPException(status_code=404, detail="not found service")
    
    return ServiceBase.model_validate(service)