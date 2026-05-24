import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# 1. DATA — bigger than 5 rows so the split actually means something
df = pd.DataFrame({
    "size":  [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200],
    "price": [50,   60,   75,   90,   100,  115,  130,  150,  160,  175]
})

# 2. FEATURES (X) AND TARGET (y)
# Double brackets on X = 2D (matrix). Single bracket on y = 1D (series).
X = df[["size"]]
y = df["price"]

# 3. TRAIN/TEST SPLIT — never evaluate on data the model has seen
# 80% train, 20% test. random_state makes the split reproducible.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. TRAIN
model = LinearRegression()
model.fit(X_train, y_train)

# 5. INSPECT WHAT THE MODEL LEARNED
# Equation: price = coef * size + intercept
print(f"Slope (coef):    {model.coef_[0]:.4f}")
print(f"Intercept:       {model.intercept_:.4f}")
print(f"Equation: price = {model.coef_[0]:.4f} * size + {model.intercept_:.4f}")

# 6. EVALUATE ON UNSEEN DATA
y_pred = model.predict(X_test)
print(f"\nR² score:        {r2_score(y_test, y_pred):.4f}")   # 1.0 = perfect, 0 = useless
print(f"Mean Abs Error:  {mean_absolute_error(y_test, y_pred):.2f}")

# 7. PREDICT ON A BRAND-NEW HOUSE
new_house_size = 1600
predicted_price = model.predict([[new_house_size]])[0]
print(f"\nPredicted price for {new_house_size} sqft: {predicted_price:.2f}")

# 8. SAVE THE TRAINED MODEL
joblib.dump(model, "my_trained_housing_model.pkl")
print("\nModel saved successfully")

# 9. LOAD IT BACK (this is what 'deployment' looks like)
loaded_model = joblib.load("my_trained_housing_model.pkl")
print(f"Loaded model predicts {new_house_size} sqft = {loaded_model.predict([[new_house_size]])[0]:.2f}")