import tensorflow as tf
import numpy as np

# Dummy training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=500, verbose=0)

# Save model
model.save("model/my_model.h5")
print("Model saved successfully")
