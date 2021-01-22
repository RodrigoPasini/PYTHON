def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

valor=[6,3,9,1,2]
dobra(valor)
print(valor)