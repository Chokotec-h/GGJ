import pygame

class Platform():
    def __init__(self,x,y,l,h,color) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)