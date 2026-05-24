# House Price ML API

A linear regression model deployed as a REST API with FastAPI, plus a minimal HTML frontend.

## 🚀 Live Demo

**Try it now (no install needed):**
👉 **https://hariprashad24.github.io/house-price-ml-api/**

Also available:
- API Swagger UI: https://house-price-ml-api.onrender.com/docs
- API root: https://house-price-ml-api.onrender.com/

> ⏱️ Note: Free-tier backend sleeps after 15 min of inactivity. First request after sleep takes ~30 seconds to wake up. After that, predictions are instant.

## Stack
- Python, scikit-learn, pandas
- FastAPI, uvicorn, pydantic
- HTML/CSS/JS frontend

## Run locally

```bash
pip install -r requirements.txt
uvicorn App:app --reload
```

Open `http://127.0.0.1:8000/docs` for the Swagger UI, or open `index.html` in a browser for the frontend.

## Endpoint

`POST /predict`

Request:
```json
{ "size": 1600 }
```

Response:
```json
{ "input_size": 1600, "predicted_price": 85.5 }
```

## Files
- `train_model.py` — trains and saves the model
- `App.py` — FastAPI server
- `my_trained_housing_model.pkl` — serialized trained model
- `index.html` — frontend client
- `requirements.txt` — dependencies

"Free tier sleeps; first request after 15 min idle takes ~30s to wake"

## Author
<<<<<<< HEAD
Hariprashad C — architect-turned-ML practitioner. Built as part of a portfolio bridging architecture and machine learning 
=======
Hariprashad C — architect-turned-ML practitioner. Built as part of a portfolio bridging architecture and machine learning 
>>>>>>> e77ce280eabecd35a58b884ce5e8a96c71740e40
