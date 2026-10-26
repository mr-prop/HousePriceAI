#  House Price Prediction

Machine Learning project for predicting house prices using Linear Regression with FastAPI, Streamlit and Docker.


## Project Overview

This project predicts house prices based on several features such as:

- Square Feet
- Bedrooms
- Bathrooms
- Floors
- Year Built
- Garage Size
- Location Score

The prediction model is served using FastAPI and the user interface is built with Streamlit.

## Demo

![Application Demo](assets/demo.gif)

## Features

- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- **Experiment Tracking & Model Metrics Logging with MLflow**
- **Data and Model Versioning with DVC**
- **Reproducible Machine Learning Pipelines**
- FastAPI REST API
- Streamlit Interactive Dashboard
- Docker Support

## Technologies

- Python
- Pandas
- NumPy
- joblib
- Scikit-learn
- FastAPI
- Streamlit
- Docker
- mlflow
- dvc

## Machine Learning Pipeline

- Data Cleaning
- Feature Engineering
- Train Test Split
- Model Training
- Model Evaluation
- Model Experiment
- Model Saving

## Model Performance

The Linear Regression model achieved strong predictive performance on the test dataset, with an **R² score of 97.45%**.

**Evaluation Metrics:**
- **R² Score:** 0.9745
- **Mean Absolute Error (MAE):** 16,769.56
- **Root Mean Squared Error (RMSE):** 20,446.03

These results indicate that the model explains approximately 97.45% of the variance in house prices, with an average absolute prediction error of approximately 16,770 price units.

The model demonstrates promising performance in predicting house prices on unseen test data. However, prediction accuracy may vary depending on the characteristics of individual properties.


## API Usage

The FastAPI REST API allows users to predict house prices by submitting property features to the trained Linear Regression model.

### Predict House Price

**Endpoint:** `POST /api/v1/predict/`

Send a JSON request containing the following house features:

**Sample Request**
```json
{
  "Square_Feet": 199.66,
  "Num_Bedrooms": 5,
  "Num_Bathrooms": 2,
  "Num_Floors": 2,
  "Year_Built": 1918,
  "Has_Garden": 0,
  "Has_Pool": 0,
  "Garage_Size": 17,
  "Location_Score": 2.07,
  "Distance_to_Center": 8.28
}
```

**Sample Response**
```json
{
  "status": "success",
  "prediction": 590848.3012306448
}
```

The API validates the input features, passes them to the trained model, and returns the predicted house price as a JSON response.

You can explore and test the API endpoints interactively through the FastAPI Swagger UI at `/docs`.



## Docker

Run

docker compose up --build

Prerequisite:
Have Docker and Docker Compose installed on your system to avoid problems.


## Run Without Docker

```bash
git clone ...
cd project

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

# Run FastAPI
uvicorn app.api:app --reload

# Run Streamlit
streamlit run app/ml_app.py
```

### Project address

Run docker compose or fastapi and streamlit simultaneously. The following links can be used.

API -> http://127.0.0.1:8000/docs

Streamlit -> http://localhost:8501/


## Streamlit
We used Streamlit to build dashboards and a web app to showcase machine learning performance.


## Author

Your Name-> amir mohammad abdol shaikhy

GitHub-> [mr-prop](https://github.com/mr-prop)
DagsHub-> [amir_abd_shai](https://dagshub.com/amir_abd_shai)

Email-> amirmohammadshai@gmail.com