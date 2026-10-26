import pandas as pd

from app.Model_Loader import model_load


class PredictionService:
    """Use the model"""
    def predict(self, input_data):

        predict_df = pd.DataFrame([input_data.model_dump()])
        print("Input received by model:")
        print(predict_df.to_string(index=False))
        print("Model feature names:", predict_df.columns.tolist())

        prediction = model_load.predict(predict_df)

        return float(prediction[0])