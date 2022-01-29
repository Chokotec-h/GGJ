from math import floor
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
        # Création des personnages
        player1 = Player(300,100,10,10,(255,0,0),0)
        player2 = Player(300,280,10,10,(0,0,255),1)
        # Création de la fenêtre
        window = pygame.display.set_mode((600,400))

        # INITIALISATION DES VARIABLES

        continuer = True
        time = 0
        timeswap = 3
        FPS = 60
        

        """ Programme principal """

        while continuer :
            # Réinitialise le fon
            window.fill((255,255,255))

            # get events
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False
            keys = pygame.key.get_pressed()
            ##

            # Niveau Test
            stage = Stage(  [Platform(0,195,350,10,(0,0,0)),Platform(340,100,10,100,(0,0,0)),Platform(340,100,100,10,(0,0,0)),Platform(290,50,10,100,(0,0,0)),Platform(300,50,100,10,(0,0,0)),Platform(0,300,600,10,(0,0,0))],
                            [Swap(200,100,5,95,(100,100,100))],
                            [Door(320,205,10,95,(100,0,0),0),Door(50,205,10,95,(0,0,100),1)])
            
            stage.draw(window)
            ##

            # Action des personnages
            player1.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],stage)
            player1.draw(window)

            player2.move(keys[K_q],keys[K_d],keys[K_z],stage)
            player2.draw(window)
            ##

            # Zones d'inversions périodiques
            if timeswap :
                time += 1
                if time/FPS % timeswap == 0 :
                    player1,player2 = swap_chars(player1,player2)
                elif (time/FPS % timeswap == timeswap/4 or
                     time/FPS % timeswap == 2*timeswap/4 or
                     time/FPS % timeswap == 3*timeswap/4) :
                    pygame.mixer.Sound("./SE/dong.mp3").play()
            ##

            # Inversion dûes aux éléments de swap
            if player1.must_swap or player2.must_swap:
                player1,player2 = swap_chars(player1,player2)
                player1.swapping,player2.swapping = True,True # empêche les inversions infinies
            ##

            # Actualisation de l'écran (60FPS)
            pygame.display.flip()
            clock.tick(FPS)
    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()