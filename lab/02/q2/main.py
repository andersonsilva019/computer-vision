import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import GeometricTransformer 
import Stickman
import sys


# Função principal
def main():
  offset_global = 22  # Define um deslocamento global de 22

  gt = GeometricTransformer.GeometricTransformer()
  stickman = Stickman.Stickman(gt, offset_global)  # Cria um objeto Stickman

  stickman_image = np.zeros((300, 300, 3), np.uint8)  # Cria uma imagem de destino preta
  stickman_image.fill(255)           # Preenche a imagem de destino com a cor branca

  line_img = cv.imread(sys.argv[1])  # Lê a imagem da linha
  circle_img = cv.imread(sys.argv[2])  # Lê a imagem do círculo

  stickman_image_height, stickman_image_width = stickman_image.shape[:2]  # Obtém as dimensões da imagem de destino

  size_arms = 0.75  # Define o tamanho dos braços
  size_legs = size_arms * 2  # Define o tamanho das pernas

  stickman.draw_head(circle_img, stickman_image)  # Desenha a cabeça na imagem de destino
  stickman.draw_body(line_img, stickman_image)  # Desenha o corpo na imagem de destino
  stickman.draw_arm_left(line_img, stickman_image, size_arms)  # Desenha o braço esquerdo na imagem de destino com escala de 0.75
  stickman.draw_arm_right(line_img, stickman_image, size_arms)  # Desenha o braço direito na imagem de destino com escala de 0.75
  stickman.draw_leg_left(line_img, stickman_image, size_legs)  # Desenha a perna esquerda na imagem de destino com escala de 1.5
  stickman.draw_leg_right(line_img, stickman_image, size_legs)  # Desenha a perna direita na imagem de destino com escala de 1.5
  
  cv.imshow('Stickman', stickman_image)  # Mostra a imagem de destino
  cv.imwrite('q2/images/stickman.jpg', stickman_image) 
  cv.waitKey(0)
  cv.destroyAllWindows()

main()  # Chama a função principal
