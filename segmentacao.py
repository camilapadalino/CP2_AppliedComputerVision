import cv2
 
PATH = "imagens/lena.jpg"
 
img = cv2.imread(PATH, 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
 
LIM, img2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(LIM)
 
cv2.namedWindow("Original", 2)
cv2.imshow("Original", img_gray)
cv2.namedWindow("Otsu", 2)
cv2.imshow("Otsu", img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()