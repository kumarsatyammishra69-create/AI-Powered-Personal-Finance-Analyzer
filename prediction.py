import joblib
import pandas as pd

def predict(amount, month, day_of_week, is_weekend):
    model = joblib.load("models/expense_model.pkl")
    le    = joblib.load("models/label_encoder.pkl")

    data = pd.DataFrame(
        [[amount, month, day_of_week, is_weekend]],
        columns=['amount', 'month', 'day_of_week', 'is_weekend']
    )

    encoded  = model.predict(data)[0]
    category = le.inverse_transform([encoded])[0]
    return category