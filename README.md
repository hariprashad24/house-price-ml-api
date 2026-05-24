# House Price ML API

A linear regression model deployed as a REST API with FastAPI, plus a minimal HTML frontend.

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

## Author
Hariprashad C — architect-turned-ML practitioner. Built as part of a portfolio bridging architecture and machine learning for M.Sc. ITECH Stuttgart 2027 application.