import cv2 as cv

class Stickman:
  def __init__(self, geometricTransformer, offsetGlobal):
    self.gt = geometricTransformer
    self.offset_global = offsetGlobal

  # Desenha a perna direita na imagem de destino
  def draw_leg_right(self,img, dst_image, scale):
    leg_right = img.copy()  # Cria uma cópia da imagem da perna direita
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    dimension = (int(leg_right.shape[1] * scale), int(leg_right.shape[0] * scale))  # Calcula as novas dimensões da perna direita
    leg_right = cv.resize(leg_right, dimension)  # Redimensiona a perna direita
    leg_right = self.gt.rotation(leg_right, -45)  # Rotaciona a perna direita
    leg_right_height, leg_right_width = leg_right.shape[:2]  # Obtém as dimensões da perna direita

    offset_y = 85
    offset_x = 43

    y_initial = (dst_image_height // 2 - leg_right_height // 2) + offset_y - self.offset_global # Calcula a coordenada y inicial da ROI para a perna direita
    y_final = (dst_image_height // 2 + leg_right_height // 2) + offset_y  - self.offset_global   # Calcula a coordenada y final da ROI para a perna direita
    x_initial = (dst_image_width // 2 - leg_right_width // 2) + offset_x  # Calcula a coordenada x inicial da ROI para a perna direita
    x_final = (dst_image_width // 2 + leg_right_width // 2) + offset_x  # Calcula a coordenada x final da ROI para a perna direita

    # ROI (Região de Interesse) para a perna direita
    roi_leg_right = dst_image[y_initial:y_final, x_initial:x_final]
    roi_leg_right = cv.resize(roi_leg_right, (leg_right_width, leg_right_height), interpolation=cv.INTER_AREA)  # Redimensiona a ROI para as dimensões da perna direita

    _, threshold = cv.threshold(cv.cvtColor(leg_right, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem da perna direita

    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(leg_right, leg_right, mask=threshold_inv)  # Aplica a máscara à imagem da perna direita
    background = cv.bitwise_and(roi_leg_right, roi_leg_right, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    image = cv.add(background, icon)  # Adiciona o ícone da perna direita à imagem de destino

    image = cv.resize(image, (leg_right_width, leg_right_height), interpolation=cv.INTER_AREA)  # Redimensiona a imagem da perna direita

    dst_image[y_initial:y_final, x_initial:x_final] = image  # Define a imagem final da perna direita na imagem de destino

  # Desenha a perna esquerda na imagem de destino
  def draw_leg_left(self,img, dst_image, scale):
    leg_left = img.copy()  # Cria uma cópia da imagem da perna esquerda
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    dimension = (int(leg_left.shape[1] * scale), int(leg_left.shape[0] * scale))  # Calcula as novas dimensões da perna esquerda
    leg_left = cv.resize(leg_left, dimension)  # Redimensiona a perna esquerda
    
    leg_left = self.gt.rotation(leg_left, 45)  # Rotaciona a perna esquerda
    leg_left_height, leg_left_width = leg_left.shape[:2]  # Obtém as dimensões da perna esquerda

    offset_y = 85
    offset_x = 43

    y_initial = (dst_image_height // 2 - leg_left_height // 2) + offset_y - self.offset_global  # Calcula a coordenada y inicial da ROI para a perna esquerda
    y_final = (dst_image_height // 2 + leg_left_height // 2) + offset_y  - self.offset_global  # Calcula a coordenada y final da ROI para a perna esquerda
    x_initial = (dst_image_width // 2 - leg_left_width // 2 )- offset_x  # Calcula a coordenada x inicial da ROI para a perna esquerda
    x_final = (dst_image_width // 2 + leg_left_width // 2) - offset_x  # Calcula a coordenada x final da ROI para a perna esquerda

    # ROI (Região de Interesse) para a perna esquerda
    roi_leg_left = dst_image[y_initial:y_final, x_initial:x_final]
    roi_leg_left = cv.resize(roi_leg_left, (leg_left_width, leg_left_height), interpolation=cv.INTER_AREA)  # Redimensiona a ROI para as dimensões da perna esquerda

    _, threshold = cv.threshold(cv.cvtColor(leg_left, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem da perna esquerda
    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(leg_left, leg_left, mask=threshold_inv)  # Aplica a máscara à imagem da perna esquerda
    background = cv.bitwise_and(roi_leg_left, roi_leg_left, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    image = cv.add(background, icon)  # Adiciona o ícone da perna esquerda à imagem de destino

    image = cv.resize(image, (leg_left_width, leg_left_height), interpolation=cv.INTER_AREA)  # Redimensiona a imagem da perna esquerda

    dst_image[y_initial:y_final, x_initial:x_final] = image  # Define a imagem final da perna esquerda na imagem de destino

  # Desenha o corpo na imagem de destino
  def draw_body(self,img, dst_image):
    body = img.copy()  # Cria uma cópia da imagem do corpo
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    body_height, body_width = body.shape[:2]  # Obtém as dimensões da imagem do corpo

    body = self.gt.rotation(body, 90)  # Rotaciona a imagem do corpo

    y_initial = dst_image_height // 2 - body_height // 2 - self.offset_global   # Calcula a coordenada y inicial da ROI para o corpo
    y_final = dst_image_height // 2 + body_height // 2 - self.offset_global    # Calcula a coordenada y final da ROI para o corpo
    x_initial = dst_image_width // 2 - body_width // 2  # Calcula a coordenada x inicial da ROI para o corpo
    x_final = dst_image_width // 2 + body_width // 2  # Calcula a coordenada x final da ROI para o corpo

    # ROI (Região de Interesse) para o corpo
    roi_body = dst_image[y_initial:y_final, x_initial:x_final]

    _, threshold = cv.threshold(cv.cvtColor(body, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem do corpo
    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(body, body, mask=threshold_inv)  # Aplica a máscara à imagem do corpo
    background = cv.bitwise_and(roi_body, roi_body, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    dst_image[y_initial:y_final, x_initial:x_final] = cv.add(background, icon)  # Adiciona o ícone do corpo à imagem de destino

  # Desenha a cabeça na imagem de destino
  def draw_head(self,img, dst_image):
    head = img.copy()  # Cria uma cópia da imagem da cabeça
    head = self.gt.translation(head, 0, -15)  # Aplica uma translação à imagem da cabeça
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    head_height, head_width = head.shape[:2]  # Obtém as dimensões da imagem da cabeça

    offset_y = 65  # Define um deslocamento na coordenada y

    # Calcula as coordenadas da ROI para a cabeça
    y_initial = (dst_image_height // 2 - head_height // 2) - offset_y   # Calcula a coordenada y inicial da ROI para a cabeça
    y_final = (dst_image_height // 2 + head_height // 2) - offset_y  # Calcula a coordenada y final da ROI para a cabeça
    x_initial = (dst_image_width // 2 - head_width // 2)  # Calcula a coordenada x inicial da ROI para a cabeça
    x_final = (dst_image_width // 2 + head_width // 2)  # Calcula a coordenada x final da ROI para a cabeça

    # ROI (Região de Interesse) para a cabeça
    roi_head =  dst_image[y_initial:y_final, x_initial:x_final]

    _, threshold = cv.threshold(cv.cvtColor(head, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem da cabeça
    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(head, head, mask=threshold_inv)  # Aplica a máscara à imagem da cabeça
    background = cv.bitwise_and(roi_head, roi_head, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    dst_image[y_initial:y_final, x_initial:x_final] = cv.add(background, icon)  # Adiciona o ícone da cabeça à imagem de destino

  # Desenha o braço esquerdo na imagem de destino
  def draw_arm_left(self,img, dst_image, scale):
    arm_left = img.copy()  # Cria uma cópia da imagem do braço esquerdo
    arm_left = self.gt.translation(arm_left, 0, -28)
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    
    dimension = (int(arm_left.shape[1] * scale), int(arm_left.shape[0] * scale))  # Calcula as novas dimensões do braço esquerdo
    arm_left = cv.resize(arm_left, dimension, interpolation=cv.INTER_AREA)  # Redimensiona o braço esquerdo
    arm_left_height, arm_left_width = arm_left.shape[:2]  # Obtém as dimensões do braço esquerdo

    offset_x = 30

    y_initial = (dst_image_height // 2 - arm_left_height // 2) - self.offset_global  # Calcula a coordenada y inicial da ROI para o braço esquerdo
    y_final = (dst_image_height // 2 + arm_left_height // 2 ) - self.offset_global  # Calcula a coordenada y final da ROI para o braço esquerdo
    x_initial = (dst_image_width // 2 - arm_left_width // 2) - offset_x  # Calcula a coordenada x inicial da ROI para o braço esquerdo
    x_final = (dst_image_width // 2 + arm_left_width // 2) - offset_x  # Calcula a coordenada x final da ROI para o braço esquerdo

    # ROI (Região de Interesse) para o braço esquerdo
    roi_arm_left = dst_image[y_initial:y_final, x_initial:x_final]
    roi_arm_left = cv.resize(roi_arm_left, (arm_left_width, arm_left_height), interpolation=cv.INTER_AREA)  # Redimensiona a ROI para as dimensões do braço esquerdo
    _, threshold = cv.threshold(cv.cvtColor(arm_left, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem do braço esquerdo

    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(arm_left, arm_left, mask=threshold_inv)  # Aplica a máscara à imagem do braço esquerdo
    background = cv.bitwise_and(roi_arm_left, roi_arm_left, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    image = cv.add(background, icon)  # Adiciona o ícone do braço esquerdo à imagem de destino

    image = cv.resize(image, (arm_left_width - 1, arm_left_height - 1), interpolation=cv.INTER_AREA)  # Redimensiona a imagem do braço esquerdo

    dst_image[y_initial:y_final, x_initial:x_final] = image  # Define a imagem final do braço esquerdo na imagem de destino

  # Desenha o braço direito na imagem de destino
  def draw_arm_right(self,img, dst_image, scale):
    arm_right = img.copy()  # Cria uma cópia da imagem do braço direito
    arm_right = self.gt.translation(arm_right, 0, -28)
    dst_image_height, dst_image_width = dst_image.shape[:2]  # Obtém as dimensões da imagem de destino
    dimension = (int(arm_right.shape[1] * scale), int(arm_right.shape[0] * scale))  # Calcula as novas dimensões do braço direito
    arm_right = cv.resize(arm_right, dimension, interpolation=cv.INTER_AREA)  # Redimensiona o braço direito
    arm_right_height, arm_right_width = arm_right.shape[:2]  # Obtém as dimensões do braço direito

    offset_x = 30

    y_initial = (dst_image_height // 2 - arm_right_height // 2) - self.offset_global  # Calcula a coordenada y inicial da ROI para o braço direito
    y_final = (dst_image_height // 2 + arm_right_height // 2) - self.offset_global   # Calcula a coordenada y final da ROI para o braço direito
    x_initial = (dst_image_width // 2 - arm_right_width // 2) + offset_x  # Calcula a coordenada x inicial da ROI para o braço direito
    x_final = (dst_image_width // 2 + arm_right_width // 2) + offset_x  # Calcula a coordenada x final da ROI para o braço direito

    # ROI (Região de Interesse) para o braço direito
    roi_arm_right = dst_image[y_initial:y_final, x_initial:x_final]
    roi_arm_right = cv.resize(roi_arm_right, (arm_right_width, arm_right_height), interpolation=cv.INTER_AREA)  # Redimensiona a ROI para as dimensões do braço direito

    _, threshold = cv.threshold(cv.cvtColor(arm_right, cv.COLOR_BGR2GRAY), 240, 255, cv.THRESH_BINARY)  # Aplica uma limiarização à imagem do braço direito
    threshold_inv = cv.bitwise_not(threshold)  # Inverte a imagem limiarizada

    icon = cv.bitwise_and(arm_right, arm_right, mask=threshold_inv)  # Aplica a máscara à imagem do braço direito
    background = cv.bitwise_and(roi_arm_right, roi_arm_right, mask=threshold)  # Aplica a máscara à região de interesse na imagem de destino

    image = cv.add(background, icon)  # Adiciona o ícone do braço direito à imagem de destino

    image = cv.resize(image, (arm_right_width - 1, arm_right_height - 1), interpolation=cv.INTER_AREA)  # Redimensiona a imagem do braço direito

    dst_image[y_initial:y_final, x_initial:x_final] = image  # Define a imagem final do braço direito na imagem de destino


