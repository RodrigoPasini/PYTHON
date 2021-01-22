núm=[2,5,9,1]
núm[2]=7 #AO CONTRÁRIO DA TUPLAS, UMA LISTA PODE SER MODIFICADA
núm.append(9)
núm.sort(reverse=True)#DEIXA EM ORDEM
núm.insert(2,2)
#núm.pop(3) DELETA O NÚMERO DA POSIÇÃO 3
if 3 in núm:
    núm.remove(3)#remove a primeira ocorrência
else:
    print("Não encontrei o número 3.")
print(núm)
print(f"Essa lista tem {len(núm)} elementos.")