

import pygame, math, random
from pygame.locals import *

#variabili globali

MAX_X = 780
MAX_XSHIP = 760
MAX_Y = 580
MIN_X = 0
MIN_Y = 0

#numero degli alieni sullo schermo
ALIENNUMBERS = 10

#definizione delle classi

class StatusDisplay(pygame.sprite.Sprite):
    #classe usata per il punteggio e le informazione nella parte alta dello schermo
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 0
        self.score = 0
        self.wave = 1
        self.font = pygame.font.SysFont("arial", 24)
        self.text = "COLPI SUBITI: %d   NEMICI COLPITI: %d  FASE NUMERO: %d" % (self.lives, self.score, self.wave)
        self.image = self.font.render(self.text, 1, (0, 0, 255))
        self.rect = self.image.get_rect()

    def update(self,lives,score,wave):

        if lives > 0:
            self.lives += 1
        elif score > 0:
            self.score += 1
        elif wave > 0:
            self.wave += 1
        
            
        self.text = "COLPI SUBITI: %d   NEMICI COLPITI: %d  FASE NUMERO: %d" % (self.lives, self.score, self.wave)
        self.image = self.font.render(self.text, 1, (0, 0, 255))
        self.rect = self.image.get_rect()





class Alien(pygame.sprite.Sprite):
    
        #classe degli alieni
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagearray=[]
        self.images = pygame.image.load('light.bmp').convert()
        self.images.set_colorkey((255,0,255))
        for i in range(0,120,24):
            self.imagearray.append(self.images.subsurface((i,0,24,24)))
        self.image = self.imagearray[0]
        self.rect = self.imagearray[0].get_rect()
        self.rect.topleft = [random.randrange(0,780),random.randrange(0,200)]
        self.direction = [random.randrange(1,5),random.randrange(1,5)]
        self.movement_ticks = 0
        self.animationcounter = random.randrange(0,4)
        self.animation_ticks = 0

    def update(self,timer):
        if self.movement_ticks < timer:
            self.movment_ticks = timer
            if self.rect.left < MIN_X or self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]

            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]

            self.movement_ticks += 20

            self.image = self.imagearray[self.animationcounter]
            if self.animation_ticks < timer:
                self.animation_ticks = timer
                self.animationcounter -= 1
                if self.animationcounter < 0:
                    self.animationcounter = 4
                self.animation_ticks += 150


class BaseShip(pygame.sprite.Sprite):
    
    #classe della nave

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('baseship.bmp').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [380,550]

    def update(self,direction):
        if direction == 0 and self.rect.left > MIN_X:
            self.rect.left -= 4
        elif direction == 1 and self.rect.left < MAX_XSHIP:
            self.rect.left += 4

class Missile(pygame.sprite.Sprite):
    
    #classe dei missili

    def __init__(self, initialposition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('missile.bmp').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = initialposition 

    def update(self):
        if self.rect.top > MIN_Y:
            self.rect.top -= 4
        else:
            self.kill()



class Explosion(pygame.sprite.Sprite):
    
    #classe per l'esplosione

    def __init__(self, initialposition):
        pygame.sprite.Sprite.__init__(self)
        self.imagearray=[]
        self.images = pygame.image.load('explosion.bmp').convert()
        self.images.set_colorkey((255,0,255))
        for i in range(0,240,60):
            self.imagearray.append(self.images.subsurface((i,0,60,60)))
        self.image = self.imagearray[0]
        self.rect = self.imagearray[0].get_rect()
        self.animation_ticks = 0
        self.animationcounter = 0
        self.rect.topleft = initialposition

    def update(self,timer):
        if self.animation_ticks < timer:
            self.animation_ticks = timer
            self.image = self.imagearray[self.animationcounter]
            self.animationcounter += 1
            if self.animationcounter > 3: self.kill()
            self.animation_ticks += 50

class Sounds():
    
    #classe per l'audio

    def __init__(self):
        pygame.mixer.pre_init(44000, 16, 2, 4096)
        self.missile = pygame.mixer.Sound('missile.wav')
        self.explosion = pygame.mixer.Sound('explosion.wav')
        self.basehit = pygame.mixer.Sound('basehit.wav')
        self.swarm = pygame.mixer.Sound('swarm.wav')

    def playmissile(self):
        self.missile.play()
    def playexplosion(self):
        self.explosions.play()
    def playbasehit(self):
        self.basehit.play()
    def playswarm(self):
        self.swarm.play()


def main():

    GAMEOVER = 0
    missileticks = 0

    WINSIZE = [800,600]
    pygame.init()

    pygame.mixer.pre_init(44000, 16, 2, 4096)
    missile = pygame.mixer.Sound('missile.wav')
    explosion = pygame.mixer.Sound('explosion.wav')
    basehit = pygame.mixer.Sound('basehit.wav')
    swarm = pygame.mixer.Sound('swarm.wav')

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINSIZE)

    aliens = pygame.sprite.RenderUpdates()

    
    i = ALIENNUMBERS
    
    while i > 0:
        aliens.add(Alien())
        i -= 1

    statusdisplay = pygame.sprite.RenderUpdates()
    statusdisplay.add(StatusDisplay())

    baseship = pygame.sprite.RenderUpdates()
    baseship.add(BaseShip())

    missiles = pygame.sprite.RenderUpdates()

    explosions = pygame.sprite.RenderUpdates()


    background = pygame.image.load('background3.bmp').convert()
    screen.blit(background,(0,0))


    pygame.display.update()

    swarm.play()


    while not GAMEOVER:

        time = pygame.time.get_ticks()

        for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]: direction = 0
        elif pressed_keys[K_RIGHT]: direction = 1
        else: direction = 3
        if pressed_keys[K_z]: fired = 1
        else: fired = 0

        if fired == 1 and time > missileticks:
            missileticks = time + 300
            a,b,c,d = rectlistbaseship[0]
            missiles.add(Missile((a+18,b)))
            missile.play()

        baseship.clear(screen,background)
        aliens.clear(screen,background)
        missiles.clear(screen,background)
        explosions.clear(screen,background)
        statusdisplay.clear(screen,background)

        baseship.update(direction)
        missiles.update()

        aliens.update(time)
        explosions.update(time)



        for i in pygame.sprite.groupcollide(aliens, missiles, True, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a-20,b-20)))
            statusdisplay.update(0,1,0)
            explosion.play()

        for i in pygame.sprite.groupcollide(baseship, aliens, False, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a-20,b-20)))
            statusdisplay.update(1,0,0)
            basehit.play()

        rectlistbaseship = baseship.draw(screen)
        rectlistmissiles = missiles.draw(screen)
        rectlistaliens = aliens.draw(screen)
        if len(rectlistaliens) == 0:
            i = ALIENNUMBERS 
            while i > 0:
                aliens.add(Alien())
                i -= 1
            statusdisplay.update(0,0,1)
            swarm.play()

        rectlistexplosions = explosions.draw(screen)
        rectliststatusdisplay = statusdisplay.draw(screen)
        pygame.display.update(rectlistbaseship)
        pygame.display.update(rectlistmissiles)
        pygame.display.update(rectlistaliens)
        pygame.display.update(rectlistexplosions)
        pygame.display.update(rectliststatusdisplay)


        clock.tick(60)



if __name__ == '__main__': main()
