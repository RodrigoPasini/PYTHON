'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
peso=float(input("Informe seu peso em kg: "))
altura=float(input("Inform sua altura em m: "))
imc=peso/(altura**2)
print("Seu IMC está em {:.2f}.".format(imc))
if imc<18.5:
    print("Você está abaixo do peso.")
elif imc<25:
    print("Vocé está com o peso ideal.")
elif imc<30:
    print("Você está com sobrepeso.")
elif imc<40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")