
import cv2
import numpy as np
from tkinter import Tk, filedialog

def subtract_background(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    mask_inv = cv2.bitwise_not(mask)

    result = cv2.bitwise_and(
        image, image, mask=mask_inv
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg")]
)

root.destroy()

if path:
    subtract_background(path)
else:
    print("No image selected!")
