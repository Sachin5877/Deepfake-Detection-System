import cv2
import os

p = r"D:\deepfake_faces\train\real"

f = os.listdir(p)[:10]

for x in f:
    fp = os.path.join(p, x)

    i = cv2.imread(fp)

    if i is not None:
        print(x, i.shape)