import cv2

cam = cv2.VideoCapture(0)

while True:
    status, frame = cam.read()
    flip = cv2.flip(frame,-1)          # -- Vertically Upside Down
    cv2.imshow("Flipped",flip)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break