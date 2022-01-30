import pygame
import traceback
from pygame.locals import *
from Level_loader import load, update
from Player import Player

from Stage import *
from functions import swap_chars

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()

pygame.init()

def reset(level):
    # Création des personnages
    player1 = Player(300,100,16,16,(30,30,30),0)
    player2 = Player(300,280,16,16,(230,230,230),1)

    # Niveau Test
    stage,timeswap,player1.rect.x,player1.rect.y,player2.rect.x,player2.rect.y = load(level)

    return stage,timeswap,player1,player2

music = pygame.mixer.music.load("./Music/main_theme.mp3")

def main():
    try :
        # Création de la fenêtre
        window = pygame.display.set_mode((800,600))
        

        # INITIALISATION DES VARIABLES

        level = "./Levels/level.tmx"

        continuer = True
        time = 0
        stage,timeswap,player1,player2 = reset(level)
        FPS = 60
        
        pygame.mixer.music.play(-1)
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

            
            stage.draw(window)
            update(stage,window)
            ##

            # Action des personnages
            player1.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],stage,player2)
            player1.draw(window)

            player2.move(keys[K_q],keys[K_d],keys[K_z],stage,player1)
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

            if player1.end and player2.end :
                continuer = False
                print("Victoire")
                full = True
                for c in stage.cookies :
                    if not c.got :
                        full = False
                if full :
                    print("Vous avez obtenu tous les cookies secrets du niveau")
            
            if player1.rect.y > 800 or player2.rect.y > 800 :
                stage,timeswap,player1,player2 = reset(level)


            # Actualisation de l'écran (60FPS)
            pygame.display.update()
            clock.tick(FPS)


    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()