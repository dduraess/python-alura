import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        letras_faltando = str(letras_acertadas.count('_'))
        print(letras_acertadas)
        print('Ainda faltam acertar {} letra(s)'.format(letras_faltando))

    if acertou:
        imprime_mensagem_vencedor()
    elif enforcou:
        imprime_mensagem_perdedor()

def imprime_mensagem_abertura():
    print("*********************************")
    print("*****Bem vindo ao jogo Forca!****")
    print("*********************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicia_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

def imprime_mensagem_vencedor():
    print("Fim do jogo: você ganhou!")


def imprime_mensagem_perdedor():
    print("Fim do jogo: você perdeu!")

if(__name__ == "__main__"):
    jogar()