import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def train_model(df):
    # Encode category labels
    le = LabelEncoder()
    df['category_encoded'] = le.fit_transform(df['category'])

    features = ['amount', 'month', 'day_of_week', 'is_weekend']
    X = df[features]
    y = df['category_encoded']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"✅ Model trained! Accuracy: {acc:.2%}")

    # Save model and encoder
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/expense_model.pkl")
    joblib.dump(le,    "models/label_encoder.pkl")
    print("✅ Model saved to models/")