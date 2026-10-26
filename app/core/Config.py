from pathlib import Path

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load params.yaml from project root
PARAMS_PATH = BASE_DIR / "params.yaml"

with PARAMS_PATH.open("r", encoding="utf-8") as file:
    params = yaml.safe_load(file)

model = params["model"]


class Settings(BaseSettings):
    # Model path from params.yaml
    MODEL_PATH: str = str(
        (BASE_DIR / model["output"]).resolve()
        if not Path(model["output"]).is_absolute()
        else Path(model["output"])
    )

    API_VERSION: str = "v1"
    PROJECT_NAME: str = "House Price Prediction API"

    ALLOWED_HOSTS: list[str] = [
        "http://localhost:8000"
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()