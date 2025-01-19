from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config import CONFIG, TORTOISE_ORM

def create_app() -> FastAPI:

    app = FastAPI(docs_url="/", title=CONFIG.APP.NAME, version=CONFIG.APP.VERSION)

    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=False,
    )
    register_views(app=app)

    return app


def get_db_uri(user : str, password : str, host : str, port : int, db_name : str):
    return f"postgres://{user}:{password}@{host}:{port}/{db_name}"

def register_views(app: FastAPI):
    from src.controllers.club import views as club_views
    from src.controllers.zone import views as zone_views
    from src.controllers.service import views as service_views
    from src.controllers.computer_config import views as computer_config_views
    
    app.include_router(router=club_views, tags=["Club Endpoints"], prefix="/api/v1/club")
    app.include_router(router=zone_views, tags=["Zone Endpoints"], prefix="/api/v1/zone")
    app.include_router(router=service_views, tags=["Service Endpoints"], prefix="/api/v1/service")
    app.include_router(router=computer_config_views, tags=["Computer Config Endpoints"], prefix="/api/v1/computer_config")