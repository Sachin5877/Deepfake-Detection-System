
import cv2
import os

p = r"D:\deepfake_faces\train\real"

img = os.listdir(p)[0]

fp = os.path.join(p, img)

i = cv2.imread(fp)

print("Image Shape:", i.shape)

cv2.imshow("Image", i)
cv2.waitKey(0)
cv2.destroyAllWindows()