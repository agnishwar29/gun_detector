import cv2
import numpy as np
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(1)

firsFrame = None
gun_exist = False

while True:
    ret, frame = camera.read()

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, 1.3,5, minSize=(100,100))

    if len(gun) > 0:
        gun_exist = True

    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

    if firsFrame is None:
        firsFrame = gray
        continue

    cv2.putText(frame, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1
                )

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    if gun_exist:
        print("guns detected")
    else:
        print("guns NOT detected")
