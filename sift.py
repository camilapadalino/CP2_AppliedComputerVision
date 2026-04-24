import cv2
 
PATH = "imagens/figura09-sift.png"
 
img = cv2.imread(PATH, 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
 
sift = cv2.SIFT_create()
kp, desc = sift.detectAndCompute(img_gray, None)
 
print(f"Keypoints detectados: {len(kp)}")
 
img_kp = cv2.drawKeypoints(img_gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
img_rich = cv2.drawKeypoints(img_gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
cv2.namedWindow("Original", 2)
cv2.imshow("Original", img_gray)
cv2.namedWindow("SIFT Keypoints", 2)
cv2.imshow("SIFT Keypoints", img_kp)
cv2.namedWindow("SIFT Rich", 2)
cv2.imshow("SIFT Rich", img_rich)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 