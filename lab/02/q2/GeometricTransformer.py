import cv2 as cv
import numpy as np

class GeometricTransformer:
    def translation(self, img, x, y):
        rows, cols, ch = img.shape  # Obtém as dimensões da imagem
        M = np.float32([[1, 0, x], [0, 1, y]])  # Cria uma matriz de transformação para translação
        return cv.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))  # Aplica a translação na imagem

    def rotation(self, img, angle):
        rows, cols, ch = img.shape  # Obtém as dimensões da imagem
        center = ((cols-1) / 2.0, (rows-1) / 2.0)  # Calcula o centro da imagem
        M = cv.getRotationMatrix2D(center, angle, 1)  # Cria uma matriz de rotação
        return cv.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))  # Aplica a rotação na imagem

    def scaling(self, img, scale):
        return cv.resize(img, None, fx=scale, fy=scale)  # Redimensiona a imagem