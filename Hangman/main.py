import random
from forca import logo, estagios, vitoria, derrota
import os

# Clear console


def clear_console(): return os.system('cls')

# Randomização da palavra a partir de dicionário IME.


def escolha_palavra():
    dic = f.read()
    palavras = list(map(str, dic.split()))
    palavra = random.choice(palavras)
    return palavra

# Checar se o chute está correto


def check_chute():
    for i, letter in enumerate(palavra):
        if letter == chute:
            palavra_player[i] = letter
            chutados.append(chute)
        else:
            continue


print(logo)
with open('dic_pt-br.txt', 'r', encoding='utf-8') as f:
    palavra = list(escolha_palavra())
    print(palavra)
    vida = 0
    chutados = list()
    palavra_player = len(palavra) * ['_']
    fim = False
    while not fim:
        chute = input("\n Digite uma letra: \n").lower()
        if chute in chutados:
            print("Você tentou essa letra, lembra? Manda outra" "\n")
        elif chute in palavra:
            check_chute()
            if palavra_player == palavra:
                fim = True
                clear_console()
        else:
            vida += 1
            print(estagios[vida])
            if vida == 6:
                fim = True
        clear_console()
        print(' '.join(palavra_player))
    if palavra_player == palavra:
        clear_console()
        print(vitoria)
    else:
        clear_console()
        print(derrota)
