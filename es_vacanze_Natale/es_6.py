

def max_min (anno_max, anno_min):     #imposto la funzione che calcola il massimo e il minimo

    if (anno_max > anno_min):
        file = open("./annual.csv", "r")   #apro il file annual.csv

        #inserisco le variabili
        massimo = -200   
        minimo = 200
        contatore = 0
        for riga in file:
            if (contatore != 0):
                lista = riga.split(',')
                if (int(lista[1]) <= anno_max and int(lista[1]) >= anno_min):
                    if (float(lista[2]) > massimo):
                        massimo = float(lista[2]) 
                    if (float(lista[2]) < minimo):
                        minimo = float(lista[2]) 
            
            contatore = contatore + 1 #aggiorno il contatore
    

        file.close()  #chiudo il file
        print ("il massimo e'", massimo)  #stampa del valore massimo
        print ("il minimo e'", minimo)    #stampa del valore minimo
 
    else:
        print('il primo anno deve essere più grande.')

file = open("./annual.csv", "r")

dizionario = {}
contatore = 0
anno = 0

for riga in file:
    if (contatore != 0):
        lista = riga.split(',') #inserisco la virgola
        if (anno != int(lista[1])):
            anno = int(lista[1])
            anomalia = float(lista[2])
        else:
            dizionario[anno]=round((float(lista[2]) + anomalia) / 2, 6) # round(numero da arrotondare, numero di cifre dopo la virgola)

    contatore = contatore + 1   #aggiorno il contatore

file.close()   #chiudo il file

max_min (int(input('Inserire l anno più recente: ')), int(input('Inserire l anno meno recente: ')))  #faccio inseire l'input all'utente