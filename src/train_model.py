import cv2
import os
import numpy as np

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

p = r"D:\deepfake_faces\train"

x = []
y = []

for c in ["real", "fake"]:
    cp = os.path.join(p, c)

    f = os.listdir(cp)[:1000]

    for n in f:
        fp = os.path.join(cp, n)

        i = cv2.imread(fp)

        if i is not None:
            i = cv2.resize(i, (128, 128))
            i = i / 255.0

            x.append(i)

            if c == "real":
                y.append(0)
            else:
                y.append(1)

x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

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

m.fit(
    x_train,
    y_train,
    epochs=3,
    batch_size=32,
    validation_data=(x_test, y_test)
)

loss, acc = m.evaluate(x_test, y_test)

print("Accuracy:", acc)
# add at end of train_model.py

m.save("models/deepfake_detector.keras")

print("Model Saved Successfully")