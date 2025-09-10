# 🩺 "Scan & Detect Health Risk from User Symptoms (with Voice Alert)"

A mini-project that predicts possible health conditions based on symptoms entered by the user — and speaks the result aloud using Python's text-to-speech. This project aims to raise awareness about common health issues like flu, cold, and fatigue, especially for people who may not realize their symptoms matter.

## 🔍 Problem Statement

In our fast-moving world, people often ignore symptoms like cough, headache, or fatigue until they worsen. There's a need for a simple, accessible, and voice-driven tool that can help people quickly check if their symptoms match any common illness.

## ✅ Solution

We built a **command-line Python tool** that:
- Accepts Yes/No input for common symptoms
- Uses a machine learning model to predict the possible illness
- Speaks the result using a built-in voice assistant (pyttsx3)

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- pyttsx3 (Text-to-Speech)

---

## 📁 Folder Structure

symptom_checker/
│
├── data/
│   └── training_data.csv          ✅ Input CSV
│
├── model/
│   └── symptom_model.pkl          ✅ This is what got created
│
├── app.py                         ✅ Your main app
├── predict.py                     ✅ Training script
├── speak.py                       ✅ Voice output
└── requirements.txt               ✅ Libraries

