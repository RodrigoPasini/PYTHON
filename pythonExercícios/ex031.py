#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia=float(input("Qual é a distância da viagem em km? "))
print("Você está prestes a fazer uma viagem de {:.f} km.".format(distancia))
if distancia<=200:
    passagem=distancia*0.50
else:
    passagem=distancia*0.45
print("O valor da passagem será de R$ {:.2f}". format(passagem))