lanche=("hamburguer", "suco", "pizza", "pudim")
#TUPLAS SÃO IMUTÁVEIS
#print(lanche)
#print(lanche[2])
#print(lanche[1:3])
#print(lanche[-2:])
#for comida in lanche:
#   print(f"Eu vou comer {comida}.")
#for cont in range(0, len(lanche)):
    #print(cont)
#    print(f"Eu vou comer {lanche[cont]} na posição {cont}.")
for pos, comida in enumerate(lanche):
   print(f"Eu vou comer {comida} na posição {pos}.")
print("Comi pra caramba!")
print(len(lanche))
print(sorted(lanche))