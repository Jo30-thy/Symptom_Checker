import joblib
import pandas as pd
from speak import speak

# Load model
model = joblib.load("model/symptom_model.pkl")

# Define input symptoms
def get_user_input():
    print("Enter 1 for Yes and 0 for No:")
    fever = int(input("Do you have fever? "))
    cough = int(input("Do you have cough? "))
    headache = int(input("Do you have headache? "))
    body_pain = int(input("Do you have body pain? "))
    fatigue = int(input("Do you feel fatigued? "))
    loss_of_smell = int(input("Do you have loss of smell? "))
    shortness_of_breath = int(input("Do you have shortness of breath? "))
    
    data = pd.DataFrame([[fever, cough, headache, body_pain, fatigue, loss_of_smell, shortness_of_breath]],
                        columns=["fever", "cough", "headache", "body_pain", "fatigue", "loss_of_smell", "shortness_of_breath"])
    return data

# Predict and respond
def predict_disease():
    user_input = get_user_input()
    prediction = model.predict(user_input)[0]
    
    print(f"\n🚨 Detected: {prediction.upper()}")
    speak(f"Warning! You may have {prediction}. Please consult a doctor.")

if __name__ == "__main__":
    predict_disease()
