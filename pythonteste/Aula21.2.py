'''PARÂMETROS OPCIONAIS'''
def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f"A soma dos valors {a}+{b}+{c}={s}")


somar(3,2,5)
somar(8,4)

'''ESCOPO DE VARIÁVEIS'''
def teste():
    x=8 #variável LOCAL
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")

#PROGRAMA PRINCIPAL
n=2 #variável GLOBAL
print(f"No programa principal n vale {n}")
teste()
print(f"No programa principal, x vale {x}") # erro pq se trata de uma variável LOCAL fora da função