import cv2
import imutils

VC = cv2.VideoCapture(0)

firstframe = None
area = 1000

while True:
    _, img = VC.read()
    text = "No object detected, Normal"

    img = imutils.resize(img, width = 1000)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothen = cv2.GaussianBlur(grayscale, (21,21), 0)
    if firstframe is None:
        firstframe = smoothen
        continue
    difference = cv2.absdiff(firstframe, smoothen)
    thresholdcvt = cv2.threshold(smoothen, 180, 255, cv2.THRESH_BINARY)[1]
    finalfixedimg = cv2.dilate(thresholdcvt, None, iterations = 2)
    contour = cv2.findContours(finalfixedimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    allcontours = imutils.grab_contours(contour)
    for x in allcontours:
        if cv2.contourArea(x) < area:
            continue
        (x,y,w,h) = cv2.boundingRect(x)
        rect = cv2.rectangle(img, (x,y), (x+w,y+h), (100, 0, 100),2)
        text= "Moving Object detected"
    print(text)
    cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 0, 90), 2)
    cv2.imshow("CAMERA", img)
    key = cv2.waitKey(10)
    print(key)
    if key == ord("q"):
        break

cam.release()
cv2.destroyyAllWindows()
