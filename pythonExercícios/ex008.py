#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m=float(input("Informe o valor em metros: "))
cm=m*100
mm=m*1000
print("O valor em metros é {}.\nO valor em centímetros é {}.\nE o valor em milímetros é {}.".format(m,cm,mm))
