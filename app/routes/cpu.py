from fastapi import APIRouter
from app.config.settings import JSON_PATH
from app.services.nas_services import read_json_file

router = APIRouter(prefix="/api/cpu", tags=["CPU"])


@router.get("/")
def get_cpu():
    data = read_json_file(JSON_PATH)

    if data.get("error"):
        return data

    return {
        "cpu": data.get("cpu", []),
        "cpu_history": data.get("cpu_history", [])
    }