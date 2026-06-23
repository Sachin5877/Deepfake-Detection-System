import cv2
import numpy as np

from tensorflow.keras.models import load_model

m = load_model("models/deepfake_detector.keras")

img_path = r"D:\deepfake_faces\Test\Fake\fake_26.jpg"

img = cv2.imread(img_path)

img = cv2.resize(img, (128, 128))

img = img / 255.0

img = np.expand_dims(img, axis=0)

p = m.predict(img)

print("Raw Prediction:", p[0][0])

if p[0][0] > 0.5:
    print("Prediction: Fake")
else:
    print("Prediction: Real")

print("Confidence:", float(p[0][0]))