#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input("Informe o salário do funcionário R$ "))
aumento=salario+(salario*(15/100))
print("O novo salário do funcionário com aumento de 15% é de R$ {:.2f}".format(aumento))
