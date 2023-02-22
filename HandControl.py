import numpy as np
import pyautogui   # Click keyboard keys programatically
import cv2     # opencv
from cvzone.HandTrackingModule import HandDetector  # detect the hand gestures and hand landmarks

cap = cv2.VideoCapture(0)    # initilizes webacam, 0-0th number webcam to be started. Laptop's default top centre webcam.

cap.set(3, 1280)  ## 3 is a propid for width
cap.set(4, 720)  ## 4 is propid for height

detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # success, img = cap.read()
    # img = cv2.flip(img, 1)
    # hands, img = detector.findHands(img)  # with draw
    success, img = cap.read()   # read the image from video capture
    img = cv2.flip(img, 1)   # flip image on verticle axis
    copiedImage = img.copy()
    another_copiedimage = copiedImage.copy()

    copiedImage = cv2.rectangle(copiedImage, (450, 220), (830, 500), (120, 0, 204), 4)
    copiedImage = cv2.line(copiedImage, (0,0), (450, 220), (120, 0, 204), 4)
    copiedImage = cv2.line(copiedImage, (830, 220), (1280, 0), (120, 0, 204), 4)
    copiedImage = cv2.line(copiedImage, (0, 720), (450, 500), (120, 0, 204), 4)
    copiedImage = cv2.line(copiedImage, (830, 500), (1280, 720), (120, 0, 204), 4)

    hands, img = detector.findHands(copiedImage)   # Detect hand in frame

    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]
        # print(len(lmlist1))
        # print(lmlist1)
        #bbox1 = hand1["bbox"]
        # print(bbox1)
        centre1 = hand1["center"]
        # print(centre1)
        fingers1 = detector.fingersUp(hand1)

        if lmlist1[9][0] < 450 and lmlist1[9][1] > 220 < lmlist1[9][1] < 500:
            print ("Inside left region")
            pyautogui.press("left")
            print("Left key pressed")
        if lmlist1[9][0] > 450 and lmlist1[9][1] < 220 and lmlist1[9][1] > 0 and lmlist1[9][0]< 830:
            print("Inside Top region")
            pyautogui.press("up")
            print("Up key pressed")
        if lmlist1[9][0] > 830 and lmlist1[9][1] < 500 and lmlist1[9][1] > 200 and lmlist1[9][0]< 1280:
            print("Inside Right region")
            pyautogui.press("right")
            print("Right key pressed")
        if lmlist1[9][0] > 450 and lmlist1[9][1] > 500 and lmlist1[9][1] < 720 and lmlist1[9][0]< 830:
            print("Inside Bottom region")
            pyautogui.press("down")
            print("Down key pressed")
        # print(fingers1)

    cv2.imshow("python game", copiedImage)   # show image on window
    cv2.waitKey(1)
cv2.destroyAllWindows()