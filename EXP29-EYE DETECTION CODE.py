import cv2

# Load image
img = cv2.imread("face.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load eye cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=8
)

# Draw rectangle around eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

# Display output
cv2.imshow("Eye Detection", img)
cv2.imwrite("eye_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
