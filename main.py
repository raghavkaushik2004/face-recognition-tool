import numpy as np
import cv2
capture = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def detect(image) :
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = classifier.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 9 )
    if face is None : 
        return image
    for (x,y,w,h) in face :
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

while True :
    r, frame = capture.read()
    frame = detect(frame)
    cv2.imshow("Face Detection Tool", frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break

capture.release()
cv2.destroyAllWindows