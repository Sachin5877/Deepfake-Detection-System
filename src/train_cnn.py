from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

m = Sequential()

m.add(Conv2D(32, (3,3), activation="relu",
             input_shape=(128,128,3)))

m.add(MaxPooling2D((2,2)))

m.add(Conv2D(64, (3,3), activation="relu"))

m.add(MaxPooling2D((2,2)))

m.add(Flatten())

m.add(Dense(128, activation="relu"))

m.add(Dense(1, activation="sigmoid"))

m.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

m.summary()