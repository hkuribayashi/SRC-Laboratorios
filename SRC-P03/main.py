import time
import random


alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def criptografar(mensagem_plana, chave_c):
    msg_criptografada = ""
    for letra in mensagem_plana:
        posicao = alfabeto.index(letra)
        nova_posicao = (posicao + chave) % 26
        msg_criptografada += alfabeto[nova_posicao]
    return msg_criptografada


def decriptografar(mensagem_criptografada, chave):
    msg_plana = ""
    for letra in mensagem_criptografada:
        posicao = alfabeto.index(letra)
        nova_posicao = (posicao - chave) % 26
        msg_plana += alfabeto[nova_posicao]
    return msg_plana


if __name__ == '__main__':
    # Processo de Cifragrem
    chave = random.randint(1, 26)
    mensagem = "hugo"
    msg_criptografada = criptografar(mensagem, chave)
    print(msg_criptografada)

    # Tentando decodificar a msg sem saber o valor da chave
    inicio = time.time()
    print("Mensagem Criptografada: {}".format(msg_criptografada))
    for chave in range(26):
        mensagem_plana = decriptografar(msg_criptografada, chave)
        print("Chave: {} | Mensagem: {}".format(chave, mensagem_plana))
    fim = time.time()
    print("Tempo Total de Execução: {}".format(fim - inicio))
