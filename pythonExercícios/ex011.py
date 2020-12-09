#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l=float(input("Informe em metros a largura da parede: "))
a=float(input("Informe a altura da parede: "))
print("A área da parede é de {}m2.\nSerá utilizado {} litros de tinta para pintar 2m2".format((l*a),((l*a)/2)))