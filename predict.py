import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("data/training_data.csv")
    X = df.drop("disease", axis=1)
    y = df["disease"]

    model = RandomForestClassifier()
    model.fit(X, y)

    # Make sure folder exists
    os.makedirs("model", exist_ok=True)

    joblib.dump(model, "model/symptom_model.pkl")
    print("✅ Model trained and saved at model/symptom_model.pkl")

if __name__ == "__main__":
    train_model()
