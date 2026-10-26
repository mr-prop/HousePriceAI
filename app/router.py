from fastapi import APIRouter, Request, status
from app.core.rate_limit import limiter
from app.schemas.request import HouseFeatures
from app.services.prediction_service import PredictionService

router = APIRouter(
    prefix="/api/v1/predict",
    tags=["Prediction"]
)

prediction_service = PredictionService()


@router.post("/", status_code=status.HTTP_200_OK)
@limiter.limit("20/minute")
def predict_house(request: Request, features: HouseFeatures):
    """Predict house price from the supplied features."""

    prediction = prediction_service.predict(features)

    return {
        "status": "success",
        "input": features.model_dump(),
        "prediction": prediction
    }
