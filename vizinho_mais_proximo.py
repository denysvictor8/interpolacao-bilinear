import numpy as np
import cv2

def reduzirVizinho(img):
    largura = img.shape[0]
    altura = img.shape[1]
    nova_matriz = np.zeros((
        int(largura/2), int(altura/2), img.shape[2]
    ));
    aux_lg = 0
    aux_at = 0

    for i in range(0, int(largura/2)):
        aux_lg = 0
        for j in range(0, int(altura/2)):
            nova_matriz[i][j] = img[aux_at][aux_lg]
            aux_lg += 2
        aux_at += 2
    return nova_matriz

def ampliarVizinho(img):
    largura = img.shape[0]
    altura = img.shape[1]
    nova_lg = int(largura * 2)
    nova_at = int(altura * 2)
    nova_matriz = np.zeros(
        (nova_lg, nova_at, img.shape[2])
    )
    aux_lg = 0
    aux_at = 0

    for i in range(0, nova_lg, 2):
        aux_lg = 0
        for j in range(0, nova_at, 2):
            nova_matriz[i][j] = img[aux_at][aux_lg]
            aux_lg += 1
        aux_at += 1

    for i in range(0, nova_lg-1, 2):
        for j in range(0, nova_at-1, 2):
            nova_matriz[i][j+1] = nova_matriz[i][j]
            nova_matriz[i+1][j] = nova_matriz[i][j]
            nova_matriz[i+1][j+1] = nova_matriz[i][j]

    return nova_matriz

def main():

    # pega uma imagem qqr
    img = cv2.imread('./soldier.jpg')
    img_reduzida = reduzirVizinho(img)
    img_ampliada = ampliarVizinho(img)

    cv2.imwrite('./imagens_resultados/reduzida-vmp.jpg', img_reduzida)
    cv2.imwrite('./imagens_resultados/ampliada-vmp.jpg', img_ampliada)

if __name__ == '__main__':
    main()
