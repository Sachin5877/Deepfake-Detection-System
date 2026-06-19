import cv2
import os
import numpy as np

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

            x.append(i)

            if c == "real":
                y.append(0)
            else:
                y.append(1)

x = np.array(x)
y = np.array(y)

print("Images Shape:", x.shape)
print("Labels Shape:", y.shape)
print("Real Images:", sum(y == 0))
print("Fake Images:", sum(y == 1))