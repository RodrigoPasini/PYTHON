#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input("QUal é o salário atual do empregado? R$ "))
if salario>1250:
    aumento=salario+(salario*0.10)
else:
    aumento=salario+(salario*0.15)
print("Quem ganhava R$ {:.2f}. Passou a ganharR$ {:.2f}.".format(salario, aumento))