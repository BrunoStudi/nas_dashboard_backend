from fastapi import APIRouter
from app.config.settings import JSON_PATH
from app.services.nas_services import read_json_file

router = APIRouter(prefix="/api/gpu", tags=["GPU"])


@router.get("/status")
def get_gpu_status():
    data = read_json_file(JSON_PATH)

    if data.get("error"):
        return data

    return data.get("gpu", {})