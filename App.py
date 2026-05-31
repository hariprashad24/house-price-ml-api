from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd


# Load the trained model ONCE at startup, not on every request
model = joblib.load("my_trained_housing_model.pkl")

app = FastAPI()

# Allow the browser to call this API from a local HTML file
# In production you'd restrict allow_origins to your real domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected request body shape
class HouseInput(BaseModel):
    size: float

# Health check — useful to confirm the server is alive
@app.get("/")
def root():
    return {"status": "ok", "message": "House price API running"}

# The actual prediction endpoint
@app.post("/predict")
def predict(data: HouseInput):
    input_df = pd.DataFrame([{"size": data.size}])
    prediction = model.predict(input_df)[0]
    return {
        "input_size": data.size,
        "predicted_price": round(float(prediction), 2)
    }