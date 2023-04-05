import numpy as np
import cv2

def interp_bilinear(img, fator_de_escala):

    # Obter as dimensoes da imagem original
    altura, largura = img.shape[:2]

    # Calcula as dimensoes da nova imagem
    nova_altura = int(altura * fator_de_escala)
    nova_largura = int(largura * fator_de_escala)

    # Criar a imagem redimensionada
    imagem_redmensionada = np.zeros((nova_altura, nova_largura, 3), dtype=np.uint8)

    # Calcula a escala vertical da imagem
    escala_y = float(altura - 1) / (nova_altura - 1)
    # Calcula a escala horizontal da imagem
    escala_x = float(largura - 1) / (nova_largura - 1)

    # Realiza-se a interpolacao bilinear nos dois lacos abaixo

    # Aqui inicia-se um loop que percorre cada linha da nova imagem.
    for y in range(nova_altura):
        # Aqui perocorre cada coluna da nova imagem
        for x in range(nova_largura):

            # Calcula a posicao x na imagem original correspondente a posicao x na nova imagem
            x_original = x * escala_x
            # Calcula a posicao y na imagem original correspondente a posicao y na nova imagem.
            y_original = y * escala_y

            # Obter os indices dos pixels vizinhos na imagem original

            # Pega o indice da coluna direita mais proxima na imagem original
            x1 = int(x_original)
            # Pega o indice da coluna direita mais proxima na imagem original
            x2 = min(x1 + 1, largura - 1)
            # Pega o indice da linha superior mais proxima na imagem original
            y1 = int(y_original)
            # Pega o indice da linha inferior mais proxima na imagem original.
            y2 = min(y1 + 1, altura - 1)

            # Obter as intensidades dos pixels vizinhos
            i1 = img[y1, x1]
            i2 = img[y1, x2]
            i3 = img[y2, x1]
            i4 = img[y2, x2]

            # Calcular as intensidades interpoladas

            # Aqui e calculado a diferença entre a posicao x atual e a coluna esquerda mais proxima da imagem original.
            dx = x_original - x1
            # Calcula-se a diferença entre a posicao y atual e a linha superior mais proxima na imagem original.
            dy = y_original - y1

            # Interpola linearmente os valores de pixel na linha superior do quadrado de interpolacao
            b1 = i1 * (1 - dx) + i2 * dx
            # Interpola linearmente os valores de pixel na linha inferior do quadrado de interpolacao
            b2 = i3 * (1 - dx) + i4 * dx

            # Interpola linearmente os valores de pixel ao longo da altura do quadrado de interpolacao
            intensidade_pixels = b1 * (1 - dy) + b2 * dy

            # Atribuir a intensidade interpolada à imagem redimensionada
            imagem_redmensionada[y, x] = intensidade_pixels

    return imagem_redmensionada

# Carregar a imagem original
img = cv2.imread('./soldier.jpg')

if img is None:
    print('Erro ao carregar a imagem.')
else:
    # Definir o fator de escala
    fator_de_escala = 2

    # Realizar a interpolação bilinear
    imagem_redmensionada = interp_bilinear(img, fator_de_escala)
    cv2.imwrite('./imagens_resultados/nova-imagem-ib.jpg', imagem_redmensionada)

    # Exibir a imagem redimensionada
    cv2.imshow('Imagem Redimensionada', imagem_redmensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()