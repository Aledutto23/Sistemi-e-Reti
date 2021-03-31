
#Python è un linguaggio orientato agli oggetti. In Python tutto è un oggetto
numero = 7 # è un oggetto ovvero una istanza della classe int

#FUNZIONI
def lamiafunzione(argomento1,argomento2):
    #codice della funzione indentato
    return argomento1+argomento2

print(f"la somma è: {lamiafunzione(4,6)}")

#COLLEZIONI: liste, tuple, dizionari
#LISTE in qualche maniera "simili" agli array del C
lista = [3,5,1,6,7]
#python style
for elemento in lista:
    print(elemento) 

print("---------------")    

#C style
lunghezza = len(lista)
for indice in range(0,lunghezza):
    print(lista[indice])    