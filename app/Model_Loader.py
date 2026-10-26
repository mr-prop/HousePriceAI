
from joblib import load
from pathlib import Path
from fastapi import HTTPException

from app.core.Config import settings

MODEL_PATH = Path(settings.MODEL_PATH)

try:
    # Load model
    model_load = load(MODEL_PATH)

except FileNotFoundError as exc:
    print(f"Model file not found: {MODEL_PATH.resolve()}")
    raise RuntimeError(
        f"Model file not found: {MODEL_PATH.resolve()}"
    ) from exc
