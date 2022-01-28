import pygame
import traceback
from pygame.mixer import *
from pygame.locals import *

from Stage import *

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()

pygame.init()

def main():
    try :
        window = pygame.display.set_mode((600,400))
        continuer = True

        while continuer :
            window.fill((255,255,255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT :
                    continuer = False

            platform = Platform(280,195,40,10,(0,0,0))
            platform.draw(window)

            pygame.display.flip()
    except :
        traceback.print_exc()
    finally :
        pygame.quit()

main()