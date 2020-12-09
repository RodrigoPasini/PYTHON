#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens=("pedra", "papel", "tesoura")
computador=randint(0,2)
print('''Suas opções:
"[0] PEDRA"
"[1] PAPEL"
"[2] TESOURA''')
jogador=int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-="*15)
print("O computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*15)
if computador==0: #computador jogou PEDRA
    if jogador==0:
        print("EMPATOU O JOGO!")
    elif jogador==1:
        print("JOGADOR GANHOU!")
    elif jogador==2:
        print("COMPUTADOR GANHOU!")
    else:
        print("\033[41mOPÇÃO INVÁLIDA!\033[m")
elif computador==1: #computador jogou PAPEL
    if jogador==1:
        print("EMPATOU O JOGO!")
    elif jogador==2:
        print("JOGADOR GANHOU!")
    elif jogador==0:
        print("COMPUTADOR GANHOU!")
    else:
        print("\033[41mOPÇÃO INVÁLIDA!\033[m")
elif computador==2: #computador jogou TESOURA
    if jogador==2:
        print("EMPATOU O JOGO!")
    elif jogador==0:
        print("JOGADOR GANHOU!")
    elif jogador==1:
        print("COMPUTADOR GANHOU!")
    else:
        print("\033[41mOPÇÃO INVÁLIDA!\033[m")






