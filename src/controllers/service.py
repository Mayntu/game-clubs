from fastapi import APIRouter

from src.dto.service import ServiceBase, CreateServiceRequest
from src.services.service import create_service, find_service

views : APIRouter = APIRouter()

@views.post("", response_model=ServiceBase, status_code=201)
async def post_service(request : CreateServiceRequest) -> ServiceBase:
    service : ServiceBase = await create_service(request=request)
    return service

@views.get("/{service_id}", response_model=ServiceBase, status_code=200)
async def get_service(service_id : str) -> ServiceBase:
    service : ServiceBase = await find_service(service_id=service_id)
    return service