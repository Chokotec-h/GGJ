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
        player1 = Player(290,100,10,10,(255,0,0))
        player2 = Player(310,100,10,10,(0,0,255))
        window = pygame.display.set_mode((600,400))
        continuer = True
        time = 0
        timeswap = True

        while continuer :
            window.fill((255,255,255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False
            keys = pygame.key.get_pressed()

            platforms = [Platform(250,195,100,10,(0,0,0)),Platform(340,100,10,100,(0,0,0)),Platform(340,100,100,10,(0,0,0)),Platform(290,50,10,100,(0,0,0)),Platform(300,50,100,10,(0,0,0))]
            for p in platforms :
                p.draw(window)

            player1.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],platforms)
            player1.draw(window)

            player2.move(keys[K_q],keys[K_d],keys[K_z],platforms)
            player2.draw(window)

            pygame.display.flip()
            clock.tick(60)
            if timeswap :
                time += 1
                if time % 120 == 0 :
                    player1,player2 = player2,player1
                    player1.color,player2.color = player2.color,player1.color
    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()