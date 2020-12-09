"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""
nome="Rodrigo Fiad Pasini"
print("Seu nome em maiúsculo é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {}".format(len(nome.strip()))," letras")
dividido=nome.split()
print("Seu primeiro nome é {}".format(dividido[0][0:]))
print("Seu primeiro nome tem {}".format(len(dividido[0]))," letras")
