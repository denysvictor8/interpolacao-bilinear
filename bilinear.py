import numpy as np
from PIL import Image

def redimensionarImagem(img):

    # imagem a ser editada
    arquivo = Image.open(img)

    original = np.asarray(arquivo)
    linhas, colunas, camadas = original.shape
    nova = np.zeros((2*linhas - 1, 2*colunas - 1, camadas))
    print("Dimensoes originais: ", original.shape)

    for camada in range(3):
        nova[:, :, camada] = redimensionarCamada(original[:, :, camada])

    # convertendo de float pra inteiro
    nova = nova.astype(np.uint8)
    print("novas dimensoes: ", nova.shape)

    resultado = Image.fromarray(nova)
    nova_imagem = "./imagens_resultados/nova-"+img
    resultado.save( nova_imagem )

def redimensionarCamada(original):

    # linhas e colunas da imagem original
    linhas, colunas = original.shape
    linhaNova = 2*linhas - 1
    colunaNova = 2*colunas - 1
    nova = np.zeros((linhaNova, colunaNova))
    # movem-se cada um dos pontos
    nova[0:linhaNova:2, 0:colunaNova:2] = original[0:linhas, 0:colunas]

    # valores das colunas
    nova[:, 1:linhaNova:2, :] = (
        nova[0:linhaNova-1:2, :] + nova[2:linhaNova:2, :]
    ) / 2
    # valores das linhas
    nova[:, 1:colunaNova:2, :] = (
        nova[0:colunaNova - 1:2, :] + nova[2:colunaNova:2, :]
    ) / 2

    return nova

img = "./mcqueen.png"
redimensionarImagem(img)