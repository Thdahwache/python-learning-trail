alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continuar = True


def codificar(texto, shift):
    texto = list(texto)
    codificado = list()
    for letra in texto:
        for i, an in enumerate(alphabet):
            if letra == an:
                codificado.append(alphabet[i+shift])
                break
            if letra == " ":
                codificado.append(" ")
                break
            else:
                continue
    print("".join(codificado))


def decodificar(texto, shift):
    texto = list(texto)
    decodificado = list()
    for letra in texto:
        for i, an in enumerate(alphabet):
            if letra == an:
                decodificado.append(alphabet[i-shift])
                break
            if letra == " ":
                decodificado.append(" ")
                break
            else:
                continue
    print("".join(decodificado))


while continuar is True:

    funcao = input("Você quer codificar, decodificar ou sair?\n").lower()
    if funcao == "sair":
        continuar = False

    elif funcao == "codificar":
        texto = input("Qual o texto?\n").lower()
        shift = int(input("Qual o número mágico?\n"))
        codificar(texto, shift)

    elif funcao == "decodificar":
        texto = input("Qual o texto?\n").lower()
        shift = int(input("Qual o número mágico?\n"))
        decodificar(texto, shift)

    else:
        print("Não entendi seu pedido, tente novamente. \n")