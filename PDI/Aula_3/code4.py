from tensorflow import keras

# Define a Keras sequential model
model = keras.Sequential()

# Define the first dense layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Define the second dense layer
model.add(keras.layers.Dense(8, activation='relu', input_shape=(16,)))

# Define the output layer
model.add(keras.layers.Dense(4))

# Print the model architecture
print(model.summary())