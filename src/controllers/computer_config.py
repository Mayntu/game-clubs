from fastapi import APIRouter

from src.dto.computer_config import ComputerConfigBase, CreateComputerConfigRequest
from src.services.computer_config import create_computer_config, find_computer_config

views : APIRouter = APIRouter()

@views.post("", response_model = ComputerConfigBase, status_code = 201)
async def post_computer_config(request : CreateComputerConfigRequest) -> ComputerConfigBase:
    computer_config : ComputerConfigBase = await create_computer_config(request = request)
    return computer_config

@views.get("/{computer_config_id}", response_model = ComputerConfigBase, status_code = 200)
async def get_computer_config(computer_config_id : str) -> ComputerConfigBase:
    computer_config : ComputerConfigBase = await find_computer_config(config_id = computer_config_id)
    return computer_config
