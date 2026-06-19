from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter(prefix="/api/ipmi", tags=["IPMI"])

LOG_FILE = Path("/logs/hdd_fan_auto.log")
HDD_COMMAND_FILE = Path("/ipmi/fan_hdd_command.txt")
GPU_COMMAND_FILE = Path("/ipmi/fan_gpu_command.txt")
STATUS_FILE = Path("/ipmi/fan_status.json")
TEMP_FILE = Path("/ipmi/ipmi_temps.json")

ALLOWED_MODES = {"auto"}


@router.get("/log")
def get_ipmi_log():
    if not LOG_FILE.exists():
        return {"lines": []}

    lines = LOG_FILE.read_text(encoding="utf-8", errors="ignore").splitlines()

    return {
        "lines": lines[-80:]
    }


@router.get("/status")
def get_ipmi_status():

    hdd_mode = "AUTO"
    gpu_mode = "AUTO"

    if HDD_COMMAND_FILE.exists():
        content = HDD_COMMAND_FILE.read_text().strip()
        if content:
            hdd_mode = content.upper()

    if GPU_COMMAND_FILE.exists():
        content = GPU_COMMAND_FILE.read_text().strip()
        if content:
            gpu_mode = content.upper()

    fans = [
        {"name": "FAN1", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN2", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN3", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN4", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN5", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN6", "rpm": "N/A", "status": "N/A"},
        {"name": "FANA", "rpm": "N/A", "status": "N/A"},
        {"name": "FANB", "rpm": "N/A", "status": "N/A"}
    ]

    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text())
            fans = data.get("fans", fans)
        except Exception:
            pass

    return {
        "hdd_mode": hdd_mode,
        "gpu_mode": gpu_mode,
        "fans": fans
    }


@router.get("/temps")
def get_ipmi_temps():
    if not TEMP_FILE.exists():
        return {"temperatures": []}

    try:
        data = json.loads(TEMP_FILE.read_text())
        return {
            "temperatures": data.get("temperatures", [])
        }
    except Exception:
        return {"temperatures": []}
    

@router.post("/fans/hdd/{value}")
def set_hdd_fan_mode(value: str):
    value = value.upper()

    if value == "AUTO":
        if HDD_COMMAND_FILE.exists():
            HDD_COMMAND_FILE.unlink()
        return {"status": "ok", "mode": "AUTO", "zone": "HDD"}

    if not value.isdigit():
        return {"status": "error", "message": "Valeur invalide"}

    pwm = int(value)

    if pwm < 40 or pwm > 100:
        return {"status": "error", "message": "La valeur doit être entre 40 et 100"}

    HDD_COMMAND_FILE.write_text(str(pwm))

    return {"status": "ok", "mode": "MANUAL", "zone": "HDD", "pwm": pwm}


@router.post("/fans/gpu/{value}")
def set_gpu_fan_mode(value: str):
    value = value.upper()

    if value == "AUTO":
        if GPU_COMMAND_FILE.exists():
            GPU_COMMAND_FILE.unlink()
        return {"status": "ok", "mode": "AUTO", "zone": "GPU"}

    if not value.isdigit():
        return {"status": "error", "message": "Valeur invalide"}

    pwm = int(value)

    if pwm < 40 or pwm > 100:
        return {"status": "error", "message": "La valeur doit être entre 40 et 100"}

    GPU_COMMAND_FILE.write_text(str(pwm))

    return {"status": "ok", "mode": "MANUAL", "zone": "GPU", "pwm": pwm}