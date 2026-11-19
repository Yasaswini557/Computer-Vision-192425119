
import cv2
from tkinter import Tk, filedialog

def count_faces(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            image, (x, y), (x+w, y+h),
            (0, 255, 0), 2
        )

    print("Number of faces:", len(faces))
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
)

root.destroy()

if image_path:
    count_faces(image_path)
else:
    print("No image selected!")
