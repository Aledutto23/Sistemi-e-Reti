# I DIZIONARI
# un dizionario è una collezione di elementi, ciascuno dei quali è costituito da una chiave e un valore
# ogni elemento di un dizionario è una coppia chiave:valore

dizionario = {1:"Antonelli", 2: "Becchis", 3: "Bianco", 4: "Bongiovanni"}

# per accedere al valore di un elemento del dizionario si utilizza la notazione nome_dizionario[chiave]
dizionario[19] = "Pagliaccio"

print(dizionario)

canzone = {"numero":1,"titolo":"Francesco Totti","autore":"Bello Figo"}
print(canzone["numero"])

file = open("instagram.csv", "r")
for riga in file:
    print[riga]

file.close()