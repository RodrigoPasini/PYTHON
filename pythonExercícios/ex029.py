#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade=float(input("Qual é a velocidade atual do carro? "))
limite=float(80)
valor=float(7)
multa=float(velocidade-limite)*valor
if velocidade<=80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("MULTADO! Você excedeu o limite permitido de 80km/h.\nVocê deve pagar a multa de R$ {:.2f}.".format(multa))
