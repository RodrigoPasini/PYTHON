'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
print("-=-"*25)
print("ANALISADOR DE TRIÂNGULO")
print("-=-"*25)
a=int(input("Primeiro segmento: "))
b=int(input("Segundo segmento: "))
c=int(input("Terceiro segmento: "))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Os segmentos acima PODEM FORMAR um triângulo. ", end="")
    if a==b==c:
        print("EQUILÁTERO!")
    elif a!=b!=c!=a:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")

else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")