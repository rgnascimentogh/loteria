import random

def jogo():
    disponiveis = [1,2,3,4,5,6,8,9,10,11,13,14,16,18,19,20,21,22,23,24,25]
    for i in range(15):
        escolhido = random.choice(disponiveis)
        print(escolhido)
        disponiveis.remove(escolhido)

jogo()

    