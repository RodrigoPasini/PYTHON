def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f"Somando os {valores} temos a {s}")

soma(5,2)
soma(2,9,4)
