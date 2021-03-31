#        0   1   2   3  4  5  6    7
lista = [23, 43, 23, 1, 5, 6, 12, 99]
#slicing di liste

print(lista[4]) #estrarre un elemento
print(lista[2:5]) #slicing dall'elemento in posizione 2 incluso, fino a quello in posizione 5 escluso
print(lista[-1]) #ultimo elemento
print(lista[0:-1])


stringa = "Itis DelPozzo"
print(stringa[0:5])
if (stringa[0]=="I"):
    print("inizia per I")
elif:
    print("Non inizia per I")  
else:
    pass



def funzione(a,b,c):
    pass

funzione(a,b,c) 


lista = [3,2,-1,6,5]

#python style
for elemento in lista:
    print(elemento)

#C style
for i in range(0, len(lista)):
    print(lista[i])

#Python style enumerator
for i, elemento in enumerate(lista):
    print(f"{i} - {elemento}")

#while
contatore = 0
while(contatore<len(lista)):
    print(lista[contatore])
    contatore = contatore + 1













