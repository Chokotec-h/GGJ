import pygame
import traceback
from pygame.mixer import *
from pygame.locals import *
from Player import Player

from Stage import *

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()

pygame.init()

def main():
    try :
        player = Player(300,100,10,10,(255,0,0))
        window = pygame.display.set_mode((600,400))
        continuer = True

        while continuer :
            window.fill((255,255,255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False
            keys = pygame.key.get_pressed()

            platforms = [Platform(250,195,100,10,(0,0,0)),Platform(340,100,10,100,(0,0,0)),Platform(290,50,10,100,(0,0,0))]
            for p in platforms :
                p.draw(window)

            player.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],platforms)
            player.draw(window)

            pygame.display.flip()
            clock.tick(60)
    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()