n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2
print("A sua média final é igual a {:.1f}.".format(m))
if m>=7:
    print("Parabéns, você foi aprovado nesta matéria!")
else:
    print("Você está em recuperação. Estude mais que você irá conseguir passar!")
