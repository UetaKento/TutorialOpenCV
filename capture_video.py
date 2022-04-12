import cv2

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):
    # https://www.shangtian.tokyo/entry/2020/04/15/220123
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'): # qを押すと終了
        break

capture.release()
cv2.destroyAllWindows()
