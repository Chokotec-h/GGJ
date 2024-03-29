import pygame
import traceback
from pygame.locals import *
from Interface import Texte
from Level_loader import load, update
from Player import Player

from Stage import *
from functions import fadein, swap_chars

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()

pygame.init()

def reset(level):
    # Création des personnages
    player1 = Player(300,100,16,16,0)
    player2 = Player(300,280,16,16,1)

    # Niveau Test
    stage,timeswap,player1.rect.x,player1.rect.y,player2.rect.x,player2.rect.y = load(level)

    return stage,timeswap,player1,player2

music = pygame.mixer.music.load("./Music/main_theme.mp3")

def main():
    try :
        # Création de la fenêtre
        window = pygame.display.set_mode((800,600))
        

        # INITIALISATION DES VARIABLES

        levelnumber = 1
        level = f"./Levels/Level{levelnumber}.tmx"

        continuer = True
        time = 0
        time_dead = 0
        stage,timeswap,player1,player2 = reset(level)
        FPS = 60
        
        pygame.mixer.music.play(-1)
        """ Programme principal """
        while continuer :
            # Réinitialise le fon
            window.fill((230,240,255))

            # get events
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False
            keys = pygame.key.get_pressed()
            ##

            
            stage.draw(window)
            update(stage,window)
            player2.draw(window)
            player1.draw(window)
            ##

            if time_dead :
                time_dead += 1
                pygame.mixer.music.set_volume(1-time_dead/125)
                if time_dead > 375 :
                    fade = 255-(time_dead-375)*2
                else :
                    fade = time_dead*2
                window.blit(fadein(fade),(0,0))
                texte1.draw(window,fade)
                texte2.draw(window,fade)

                if time_dead == 375 :
                    stage,timeswap,player1,player2 = reset(level)
                    time = 0

                if time_dead > 500 :
                    time_dead = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(1)
            else :
                # Action des personnages
                player1.move(keys[K_LEFT],keys[K_RIGHT],keys[K_UP],stage,player2)

                player2.move(keys[K_q],keys[K_d],keys[K_z],stage,player1)
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
                    

                    levelnumber += 1
                    level = f"./Levels/Level{levelnumber}.tmx"
                    try :
                        pygame.mixer.Sound("./Music/bruitage/pause in.mp3").play()
                        stage,timeswap,player1,player2 = reset(level)
                        time = 0
                    except :
                        continuer = False
                        print("Fin du jeu")
                        full = True
                        for c in stage.cookies :
                            if not c.got :
                                full = False
                        if full :
                            print("Vous avez obtenu tous les cookies secrets du jeu")
            
                if player1.rect.y > 800 or player2.rect.y > 800 :
                    time_dead = 1
                    if player1.rect.y > 800 :
                        texte1 = Texte("Only remaineth thine very image lost in the light ;", ("inkfree",30,True,True),(255,255,255),400,280,800)
                        texte2 = Texte("Thou went beyondth the reach of the sight...", ("inkfree",30,True,True),(255,255,255),400,320,800)
                    if player2.rect.y > 800 :
                        texte1 = Texte("Far, far away went thine reflect ;", ("inkfree",30,True,True),(255,255,255),400,280,800)
                        texte2 = Texte("Thou remaineth empty as a [Nonetype object]...", ("inkfree",30,True,True),(255,255,255),400,320,800)


            # Actualisation de l'écran (60FPS)
            pygame.display.update()
            clock.tick(FPS)


    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()