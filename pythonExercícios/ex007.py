#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1=float(input("Informe a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
soma=n1+n2
media=soma/2
print("A soma das notas é = {}.\nA média das notas é = {:.1f}.".format(soma,media))