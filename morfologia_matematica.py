import cv2
import numpy as np

PATH = "imagens/frutas-morfologia.png"

# Lê a imagem
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

# Binariza a imagem para operações morfológicas
_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Define o elemento estruturante (kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# EROSÃO — remove pequenos objetos / afina bordas
erosao = cv2.erode(img_bin, kernel, iterations=1)

# DILATAÇÃO — preenche buracos / engrossa bordas
dilatacao = cv2.dilate(img_bin, kernel, iterations=1)

# ABERTURA (erosão seguida de dilatação) — remove ruído
abertura = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

# FECHAMENTO (dilatação seguida de erosão) — fecha buracos
fechamento = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)


# Define janelas de visualização
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binarizada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erosao", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilatacao", cv2.WINDOW_NORMAL)
cv2.namedWindow("Abertura", cv2.WINDOW_NORMAL)
cv2.namedWindow("Fechamento", cv2.WINDOW_NORMAL)


# Exibe as imagens
cv2.imshow("Original",   img)
cv2.imshow("Binarizada", img_bin)
cv2.imshow("Erosao",     erosao)
cv2.imshow("Dilatacao",  dilatacao)
cv2.imshow("Abertura",   abertura)
cv2.imshow("Fechamento", fechamento)

cv2.waitKey(0)
cv2.destroyAllWindows()
