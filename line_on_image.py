import cv2
try:
    blueimg = cv2.imread('blueImage.jpg', cv2.IMREAD_COLOR)
    if blueimg is None:
        print('ファイルを読み込めません。')
        import sys
        sys.exit()

    cv2.line(blueimg, (50, 50), (200, 50), (255, 0, 0))
    cv2.line(blueimg, (50, 100), (200, 100), (0, 255, 0), 5)
    cv2.imwrite('LineOnImage.jpg', blueimg)

    cv2.imshow('Bimg', blueimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
