import cv2
import numpy as np

PATH = "imagens/figura26a-pdi.png"

# Lê a imagem
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread(PATH)

# NEGATIVO
negativo = cv2.bitwise_not(img)

# BRILHO E CONTRASTE (alpha = contraste, beta = brilho)
brilho_contraste = cv2.convertScaleAbs(img, alpha=1.5, beta=50)

# FILTRO DE MÉDIA
media = cv2.blur(img, (5, 5))

# FILTRO GAUSSIANO
gaussiano = cv2.GaussianBlur(img, (5, 5), 0)

# FILTRO MEDIANA
mediana = cv2.medianBlur(img, 5)

# EQUALIZAÇÃO DE HISTOGRAMA
hist_eq = cv2.equalizeHist(img)

# Define janelas de visualização
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Negativo", cv2.WINDOW_NORMAL)
cv2.namedWindow("Brilho/Contraste", cv2.WINDOW_NORMAL)
cv2.namedWindow("Filtro Media", cv2.WINDOW_NORMAL)
cv2.namedWindow("Filtro Gaussiano", cv2.WINDOW_NORMAL)
cv2.namedWindow("Filtro Mediana", cv2.WINDOW_NORMAL)
cv2.namedWindow("Equalizacao Hist", cv2.WINDOW_NORMAL)

# Exibe as imagens
cv2.imshow("Original", img)
cv2.imshow("Negativo", negativo)
cv2.imshow("Brilho/Contraste", brilho_contraste)
cv2.imshow("Filtro Media", media)
cv2.imshow("Filtro Gaussiano", gaussiano)
cv2.imshow("Filtro Mediana", mediana)
cv2.imshow("Equalizacao Hist", hist_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
