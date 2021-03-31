import pygame
import sys #nativa = preinstallata
import csv

DIMENSIONI = (600, 600)
NERO = (0,0,0)
BIANCO = (255, 255, 255)


codifica = {0: [0,0,0,0,0], 1: [0,0,0,0,1], 2: [0,0,0,1,0], 3: [0,0,0,1,1], 4: [0,0,1,0,0],      # dizionario
            5: [0,0,1,0,1], 6: [0,0,1,1,1], 7: [0,1,0,0,0], 8: [0,1,0,0,1], 9: [0,1,0,1,0],
            'a': [0,1,0,1,1], 'b': [0,1,1,0,0], 'c': [0,1,1,0,1], 'd': [0,1,1,1,0], 'e': [0,1,1,1,1],
            'f': [1,0,0,0,0], 'g': [1,0,0,0,1], 'h': [1,0,0,1,0], 'i': [1,0,0,1,1], 'l': [1,0,1,0,1],
            'm': [1,0,1,1,0], 'n': [1,0,1,1,1], 'o': [1,1,0,0,0], 'p': [1,1,0,0,1], 'q': [1,1,0,1,0],
            'r': [1,1,0,1,1], 's': [1,1,1,0,0], 't': [1,1,1,0,1], 'u': [1,1,1,1,0], 'v': [1,1,1,1,1],
            'z': [1,0,1,0,0], " ": [1,0,1,0,0]}




stringa = input("inserire la stringa:")

for elemento in stringa:   
    print(codifica)


def disegnaQR():
    dimensione = 20
    for x in range(0, DIMENSIONI[0], dimensione):
        for y in range(0, DIMENSIONI[1], dimensione):
            casella = pygame.Rect(x,y,dimensione,dimensione)
            pygame.draw.rect(finestra, BIANCO, casella, 1)

        spazio = pygame.Rect(0,200,cod,dimensione)
        pygame.draw.rect(finestra, BIANCO, spazio)    

    
    



def main():
    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIMENSIONI)
    finestra.fill(NERO)
    while True:
        disegnaQR()
        #ciclo for che gestisce gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()    

if __name__=="__main__":
    main()





