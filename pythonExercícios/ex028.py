#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0,5) #Esse comando faz o computador escolher um número
#print("Pensei no número... {}.".format(computador))
print("-=-" *20)
print("Vou pensar em um número entre 0 e 5.Tente advinhar...")
print("-=-"*20)
jogador=int(input("Em que número eu pensei? ")) #jogador tenta adivinhar
print("Processando...")
sleep(2)
if jogador==computador:
    print("Você está com sorte. Acertou o número que o computador pensou.")
else:
    print("ERROOOOOOOOOOOOOU. Pensar como computador é para poucos.")
    print("O número que o computador escolheu foi {}.". format(computador))