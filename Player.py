import pygame

class Player():
    def __init__(self,x,y,l,h,color) -> None:
        self.rect = pygame.rect(x,y,l,h)
        self.color = color