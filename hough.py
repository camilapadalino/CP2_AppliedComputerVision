import cv2
import numpy as np

PATH = "imagens/linhas-mundo04-hough.png"

img  = cv2.imread(PATH, 1)
img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

LIM, img2 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print(LIM)

img3 = cv2.Canny(img2, threshold1=150, threshold2=200, apertureSize=3, L2gradient=False)

lines = cv2.HoughLinesP(img3, rho=1, theta=np.pi/180, threshold=10, minLineLength=10, maxLineGap=10)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.namedWindow("Original", 2)
cv2.imshow("Original", img1)
cv2.namedWindow("Segmentada", 2)
cv2.imshow("Segmentada", img2)
cv2.namedWindow("Bordas", 2)
cv2.imshow("Bordas", img3)
cv2.namedWindow("LINHAS", 2)
cv2.imshow("LINHAS", img)

cv2.waitKey(0)
cv2.destroyAllWindows()