
n = int(input("inserire il numero di elementi : "))
array = []
for i in range(n):
    valore = int(input("inserire il %d  elemento : " %i))
    array.append(valore)

for d in range(n -1):
    for c in range(n - d - 1):
        if(array[c] > array[c + 1]):
             swap = array[c]
             array[c] = array[c + 1]
             array[c + 1] = swap

print("array ordinato : ", array)