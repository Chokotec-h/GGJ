import pygame
import traceback
from pygame.mixer import *
from pygame.locals import *
from Player import Player

from Stage import *
from functions import swap_chars

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()

pygame.init()

def main():
    try :
        player1 = Player(300,100,10,10,(255,0,0),0)
        player2 = Player(300,280,10,10,(0,0,255),1)
        window = pygame.display.set_mode((600,400))
        continuer = True
        time = 0
        timeswap = False

        while continuer :
            window.fill((255,255,255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False
            keys = pygame.key.get_pressed()

            platforms = [Platform(0,195,350,10,(0,0,0)),Platform(340,100,10,100,(0,0,0)),Platform(340,100,100,10,(0,0,0)),Platform(290,50,10,100,(0,0,0)),Platform(300,50,100,10,(0,0,0)),Platform(0,300,600,10,(0,0,0))]
            for p in platforms :
                p.draw(window)
            
            swaps = [Swap(200,100,5,95,(100,100,100))]
            for s in swaps :
                s.draw(window)

            doors = [Door(320,205,10,95,(100,0,0),0),Door(50,205,10,95,(0,0,100),1)]
            for d in doors :
                d.draw(window)

            player1.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],platforms,swaps,doors)
            player1.draw(window)

            player2.move(keys[K_q],keys[K_d],keys[K_z],platforms,swaps,doors)
            player2.draw(window)

            pygame.display.flip()
            clock.tick(60)
            if timeswap :
                time += 1
                if time % 120 == 0 :
                    player1,player2 = swap_chars(player1,player2)
            if player1.must_swap or player2.must_swap:
                player1,player2 = swap_chars(player1,player2)
                player1.swapping,player2.swapping = True,True
    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()