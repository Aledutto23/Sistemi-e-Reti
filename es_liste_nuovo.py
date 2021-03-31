lista = [1,2,3,4,1,6,2,8]

for i, n in enumerate(lista):
    for j, m in enumerate(lista):
        if n == m and (i>j):
            print("Doppione")
