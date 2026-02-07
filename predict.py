
import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model("model/my_model.h5")

# Sample input
input_data = np.array([10], dtype=float)

# Prediction
prediction = model.predict(input_data)

print("Input:", input_data[0])
print("Prediction:", prediction[0][0])
