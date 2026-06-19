import cv2
import os

p = r"D:\deepfake_faces\train\real"

f = os.listdir(p)[0]

fp = os.path.join(p, f)

img = cv2.imread(fp)

r = cv2.resize(img, (128, 128))

n = r / 255.0

print("Original Shape:", img.shape)
print("Resized Shape:", r.shape)
print("Min Value:", n.min())
print("Max Value:", n.max())