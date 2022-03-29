import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
#Escolha player e computador
escolha = None
v = 0
d = 0
e = 0

#Outcomes

#pedra


def pedra_empate():
    global e
    print(
        f"Você escolheu:\n\n {pedra} \n\n O jogo escolheu: {pedra} \n\n Vocês empataram!")
    e += 1


def pedra_derrota():
    global d
    print(
        f"Você escolheu:\n\n {pedra} \n\n O jogo escolheu: {papel} \n\n Você perdeu!")
    d += 1


def pedra_vitoria():
    global v
    print(
        f"Você escolheu:\n\n {pedra} \n\n O jogo escolheu: {tesoura} \n\n Você ganhou!")
    v += 1
#papel


def papel_empate():
    global e
    print(
        f"Você escolheu:\n\n {papel} \n\n O jogo escolheu: {papel} \n\n Vocês empataram!")
    e += 1


def papel_derrota():
    global d
    print(
        f"Você escolheu:\n\n {papel} \n\n O jogo escolheu: {tesoura} \n\n Você perdeu!")
    d += 1


def papel_vitoria():
    global v
    print(
        f"Você escolheu:\n\n {papel} \n\n O jogo escolheu: {pedra} \n\n Você ganhou!")
    v += 1
#tesoura


def tesoura_empate():
    global e
    print(
        f"Você escolheu:\n\n {tesoura} \n\n O jogo escolheu: {tesoura} \n\n Vocês empataram!")
    e += 1


def tesoura_derrota():
    global d
    print(
        f"Você escolheu:\n\n {tesoura} \n\n O jogo escolheu: {pedra} \n\n Você perdeu!")
    d += 1


def tesoura_vitoria():
    global v
    print(
        f"Você escolheu:\n\n {tesoura} \n\n O jogo escolheu: {papel} \n\n Você ganhou!")
    v += 1


while escolha != "sair":
    escolha = input(
        "Pedra, papel ou tesoura? Digite sair para terminar ").lower()
    computador = random.randint(0, 2)

    if escolha == "pedra":
        escolha = 0
    elif escolha == "papel":
        escolha = 1
    elif escolha == "tesoura":
        escolha = 2
    elif escolha == "sair":
        print(
            f"\nVocê ganhou {v} vezes, perdeu {d} vezes e empatou {e} com o computador, parabéns!")
        break

    #Lista e resultado final

    pedra_resultados = [pedra_empate, pedra_derrota, pedra_vitoria]
    papel_resultados = [papel_vitoria, papel_empate, papel_vitoria]
    tesoura_resultados = [tesoura_derrota, tesoura_vitoria, tesoura_empate]

    resultados = [pedra_resultados, papel_resultados, tesoura_resultados]

    fim = resultados[escolha][computador]()

    print("")
