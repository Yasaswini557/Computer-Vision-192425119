
import cv2
import numpy as np

w = int(input("Enter image width: "))
h = int(input("Enter image height: "))

img = np.zeros((h, w, 3), dtype=np.uint8)
img[:] = (255, 255, 255)

bw = w // 10
bh = h // 10

# Four colored corner boxes
cv2.rectangle(img, (0, 0), (bw, bh), (0, 0, 0), -1)
cv2.rectangle(img, (w-bw, 0), (w-1, bh), (255, 0, 0), -1)
cv2.rectangle(img, (0, h-bh), (bw, h-1), (0, 255, 0), -1)
cv2.rectangle(img, (w-bw, h-bh), (w-1, h-1), (0, 0, 255), -1)

print("Colored boxes created!")

cv2.imshow("Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
