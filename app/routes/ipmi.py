from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter(prefix="/api/ipmi", tags=["IPMI"])

LOG_FILE = Path("/logs/hdd_fan_auto.log")
COMMAND_FILE = Path("/ipmi/fan_command.txt")
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
    mode = "AUTO"

    if COMMAND_FILE.exists():
        content = COMMAND_FILE.read_text().strip()
        if content:
            mode = content.upper()

    fans = [
        {"name": "FAN3", "rpm": "N/A", "status": "N/A"},
        {"name": "FAN4", "rpm": "N/A", "status": "N/A"},
        {"name": "FANA", "rpm": "N/A", "status": "N/A"},
    ]

    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text())
            fans = data.get("fans", fans)
        except Exception:
            pass

    return {
        "mode": mode,
        "fans": fans
    }


@router.post("/fans/{mode}")
def set_fan_mode(mode: str):
    mode = mode.lower()

    if mode == "auto":
        COMMAND_FILE.write_text("auto")
        return {
            "success": True,
            "message": "Mode automatique demandé"
        }

    if not mode.isdigit():
        return {
            "success": False,
            "message": "Valeur PWM invalide"
        }

    pwm = int(mode)

    if pwm < 40 or pwm > 100:
        return {
            "success": False,
            "message": "La PWM doit être entre 40 et 100%"
        }

    COMMAND_FILE.write_text(str(pwm))

    return {
        "success": True,
        "message": f"Mode manuel demandé : {pwm}%"
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