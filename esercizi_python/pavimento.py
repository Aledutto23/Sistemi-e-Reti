import pygame
import sys #nativa = preinstallata
DIMENSIONI = (600, 500)
NERO = (0,0,0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

def drawgrid():
    dimensione = 100
    for x in range(0, DIMENSIONI[0], dimensione):
        for y in range(0, DIMENSIONI[1], dimensione):
            piastrella = pygame.Rect(x,y,dimensione,dimensione)
            pygame.draw.rect(finestra, BIANCO, piastrella, 1)

    ostacolo1 = pygame.Rect(0,200,dimensione,dimensione)
    ostacolo2 = pygame.Rect(0,0,200,dimensione)
    ostacolo3 = pygame.Rect(400,100,dimensione,dimensione)
    ostacolo4 = pygame.Rect(200,200,dimensione,300)
    ostacolo5 = pygame.Rect(400,300,dimensione,dimensione)

    pygame.draw.rect(finestra, ROSSO, ostacolo1)
    pygame.draw.rect(finestra, ROSSO, ostacolo2)
    pygame.draw.rect(finestra, ROSSO, ostacolo3)
    pygame.draw.rect(finestra, ROSSO, ostacolo4)
    pygame.draw.rect(finestra, ROSSO, ostacolo5)
    
    
    

def main():
    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIMENSIONI)
    finestra.fill(NERO)
    while True:
        drawgrid()
        #ciclo for che gestisce gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()    

if __name__=="__main__":
    main()
