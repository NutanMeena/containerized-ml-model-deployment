from fastapi import FastAPI
import tensorflow as tf
import numpy as np

# Create API object
app = FastAPI()

# Load trained model
model = tf.keras.models.load_model("model/my_model.h5")

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict(value: float):
    input_data = np.array([[value]])
    prediction = model.predict(input_data)
    return {
        "input": value,
        "prediction": float(prediction[0][0])
    }
