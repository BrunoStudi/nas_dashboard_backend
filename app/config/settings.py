import os
from dotenv import load_dotenv

load_dotenv()

JSON_PATH = os.getenv("JSON_PATH", "./nas_status.json")