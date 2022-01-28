import pygame

class Swap():
    def __init__(self,x,y,l,h,color) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

class Door():
    def __init__(self,x,y,l,h,color,number) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color
        self.number = number # numéro du personnage qui peut passer

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

class Platform():
    def __init__(self,x,y,l,h,color) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)