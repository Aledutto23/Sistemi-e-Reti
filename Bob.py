import pygame
import csv
import sys
import random

DIM = (600,500)
SFONDO = (0,0,0)
LINEA = (255,255,255)


def drawlinea():
    dim = 20
    spessore = 1
    direzioni = 60

    dizionario_posizioni = {0:[0,0], 1:[10,0], 2:[20,0], 3:[20,-10]}
    dizionario_posizioni.items()
    
    for direzioni in dizionario_posizioni.items():
        linea = pygame.Rect(300,250,dim,spessore)
        print(direzioni)
    

    pygame.draw.rect(finestra, LINEA, linea)
    
    with  open("file.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for chiave, valore in dizionario_posizioni.items():
            lista = [chiave, valore[0], valore[1]]
            csvwriter.writerow(lista)


pygame.init()
global finestra
finestra = pygame.display.set_mode(DIM)
finestra.fill(SFONDO)

while True:
    drawlinea()    
     #ciclo for che gestisce gli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()   



