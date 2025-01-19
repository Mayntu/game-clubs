from fastapi.exceptions import HTTPException
from uuid import UUID

from src.dto.computer_config import (
    ComputerConfigBase,
    CreateComputerConfigRequest
)
from src.models.models import ComputerConfig

async def create_computer_config(request: CreateComputerConfigRequest) -> ComputerConfigBase:
    try:
        computer_config : ComputerConfig = await ComputerConfig.create(
            cpu=request.cpu,
            gpu=request.gpu,
            ram=request.ram,
            keyboard=request.keyboard,
            mouse=request.mouse,
            headset=request.headset,
            armchair=request.armchair,
            monitor=request.monitor,
            internet=request.internet
        )
    except:
        raise HTTPException(status_code=400, detail="not valid computer configuration parameters")

    return ComputerConfigBase.from_orm(computer_config)


async def find_computer_config(config_id: str) -> ComputerConfigBase:
    try:
        computer_config: ComputerConfig = await ComputerConfig.get(id=UUID(config_id))
    except:
        raise HTTPException(status_code=404, detail="not found computer configuration")
    
    return ComputerConfigBase.model_validate(computer_config)