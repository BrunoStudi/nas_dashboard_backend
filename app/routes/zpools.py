from fastapi import APIRouter
from app.config.settings import JSON_PATH
from app.services.nas_services import read_json_file

router = APIRouter(prefix="/api/zpools", tags=["ZPools"])


@router.get("/")
def get_zpools():
    data = read_json_file(JSON_PATH)

    if data.get("error"):
        return data

    return data.get("zpools", [])