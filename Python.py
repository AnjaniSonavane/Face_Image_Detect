import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('C:\\Users\\Anjani\\Pictures\\Anjani.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print(faces)
# Resize image
# new_dimension = (100, 100)
# img_resized = cv2.resize(img, new_dimension)
#Image might get distorted with the use of above code

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

t = time.time()
cv2.putText(img, "Hello", (20,20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 0),2)
print(str(time.time() - t))

# Display the output
cv2.imshow('img', img)
cv2.waitKey()

