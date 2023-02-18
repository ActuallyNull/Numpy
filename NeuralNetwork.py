import tensorflow as tf
from keras import layers
import random

# Training data
randInt = random.randint(0,1)
x_train = [[randInt, randInt], [randInt, randInt], [randInt, randInt], [randInt, randInt]]
y_train = [[randInt], [randInt], [randInt], [randInt]]

# Validation data
x_val = [[1, 1], [1, 1], [1, 1], [1, 1]]
y_val = [[1], [1], [1], [1]]

# Define the neural network architecture
model = tf.keras.Sequential([
  layers.Dense(32, activation='relu', input_shape=(2,)),
  layers.Dense(16, activation='sigmoid', input_shape=(2,)),
  layers.Dense(1)
])

# Compile the model with the loss function, optimizer, and metrics
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=['accuracy'])

# Train the model on the training data
model.fit(x_train, y_train, epochs=50, validation_data=(x_val, y_val))