#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''for contagem in range(1,51):
    if contagem%2==0:'''
for contagem in range(2,51,2):
        print(contagem, end=", ")
print("FIM")