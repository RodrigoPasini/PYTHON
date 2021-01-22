'''ESCOPO DE VARIÁVEIS'''
#INÍCIO ESCOPO GLOBAL
def teste(b):#INÍCIO ESCOPO LOCAL
    global a#A de fora passa a valer 8
    a=8
    b+=4
    c=2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")#FIM ESCOPO LOCAL

a=5
teste(a)
print(f"A fora vale {a}")#FIM ESCOPO GLOBAL