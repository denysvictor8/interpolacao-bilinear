import numpy as np
import cv2

def interp_bilinear(img, fator_de_escala):
    # Obter as dimensões da imagem original
    altura, largura = img.shape[:2]

    # Calcular as novas dimensões
    nova_altura = int(altura * fator_de_escala)
    nova_largura = int(largura * fator_de_escala)

    # Criar a imagem redimensionada
    imagem_redmensionada = np.zeros((nova_altura, nova_largura, 3), dtype=np.uint8)

    # Obter os fatores de escala em relação às dimensões originais
    escala_y = float(altura - 1) / (nova_altura - 1)
    escala_x = float(largura - 1) / (nova_largura - 1)

    # Realizar a interpolação bilinear
    for y in range(nova_altura):
        for x in range(nova_largura):
            # Calcular as coordenadas na imagem original
            x_original = x * escala_x
            y_original = y * escala_y

            # Obter os índices dos pixels vizinhos na imagem original
            x1 = int(x_original)
            x2 = min(x1 + 1, largura - 1)
            y1 = int(y_original)
            y2 = min(y1 + 1, altura - 1)

            # Obter as intensidades dos pixels vizinhos
            i1 = img[y1, x1]
            i2 = img[y1, x2]
            i3 = img[y2, x1]
            i4 = img[y2, x2]

            # Calcular as intensidades interpoladas
            dx = x_original - x1
            dy = y_original - y1
            b1 = i1 * (1 - dx) + i2 * dx
            b2 = i3 * (1 - dx) + i4 * dx
            intensidade_pixels = b1 * (1 - dy) + b2 * dy

            # Atribuir a intensidade interpolada à imagem redimensionada
            imagem_redmensionada[y, x] = intensidade_pixels

    return imagem_redmensionada

# Carregar a imagem original
img = cv2.imread('./borboleta.jpg')
# img = cv2.imread('./mcqueen.jpg')

if img is None:
    print('Erro ao carregar a imagem.')
else:
    # Definir o fator de escala
    fator_de_escala = 2

    # Realizar a interpolação bilinear
    imagem_redmensionada = interp_bilinear(img, fator_de_escala)
    cv2.imwrite('./imagens_resultados/nova-imagem.jpg', imagem_redmensionada)

    # Exibir a imagem redimensionada
    cv2.imshow('Imagem Redimensionada', imagem_redmensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()