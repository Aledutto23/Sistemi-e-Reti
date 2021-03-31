OSTACOLO = -1

CELLE_ADIACENTI = [-1,0],[0,1],[1,0],[0,-1]

def controlla_celle_adiacenti(p,x,y):
    #scorro su celle adiacenti


def numero_piastrelle_libere(p):
    pavimento_numerato = []

    contatore = -1
    for riga in p:
        nuova_riga = []
        for piastrella in riga:
            if piastrella == 0:  #libero
                contatore = contatore + 1
                nuova_riga.append(contatore)
            else:
                nuova_riga.append(OSTACOLO)
        pavimento_numerato.append(nuova_riga)
    return pavimento_numerato


def main():   
    pavimento = [[1,1,0,0,0,0],
             [0,0,0,0,1,0],
             [1,0,1,0,0,0],
             [0,0,1,0,1,0],
             [0,0,1,0,0,0]]
    print(numero_piastrelle_libere(pavimento))


    
if __name__=="__main__":
    main()







