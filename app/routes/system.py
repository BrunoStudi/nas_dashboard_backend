from fastapi import APIRouter
from app.config.settings import JSON_PATH
from app.services.nas_services import read_json_file

router = APIRouter(prefix="/api/system", tags=["System"])

def parse_size_to_tb(value: str) -> float:
    if not value or value == "N/A":
        return 0.0

    value = value.strip().upper().replace("IB", "").replace("B", "")

    try:
        if value.endswith("T"):
            return float(value[:-1])
        if value.endswith("G"):
            return float(value[:-1]) / 1024
        if value.endswith("M"):
            return float(value[:-1]) / 1024 / 1024
    except ValueError:
        return 0.0

    return 0.0

@router.get("/info")
def get_system_info():
    data = read_json_file(JSON_PATH)

    if data.get("error"):
        return data

    cpu = data.get("cpu", {})
    memory = data.get("memory", {})

    zpools = data.get("zpools", [])

    storage_total_tb = sum(parse_size_to_tb(pool.get("size", "0")) for pool in zpools)
    storage_used_tb = sum(parse_size_to_tb(pool.get("allocated", "0")) for pool in zpools)
    storage_free_tb = sum(parse_size_to_tb(pool.get("free", "0")) for pool in zpools)

    storage_percent = round((storage_used_tb / storage_total_tb) * 100) if storage_total_tb > 0 else 0

    return {
        "cpu_model": cpu.get("model", "N/A"),
        "cpu_current_ghz": cpu.get("cpu_current_ghz", "N/A"),
        "ram_total": data.get("memory", {}).get("total", "N/A"),
        "ram_used": memory.get("used", "N/A"),
        "ram_available": memory.get("available", "N/A"),
        "storage": {
            "total_tb": round(storage_total_tb, 1),
            "used_tb": round(storage_used_tb, 1),
            "free_tb": round(storage_free_tb, 1),
            "percent": storage_percent
        }
    }
