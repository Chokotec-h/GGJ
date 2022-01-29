import pygame

class Swap():
    def __init__(self,x,y,l,h,sprite) -> None:
        """ Objet inversant la position des deux personnages """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite

    def draw(self,window):
        """ Dessine le swap 
        Entrée : fenêtre 
        Sortie : Aucune """
        window.blit(self.sprite,self.rect)

class Door():
    def __init__(self,x,y,l,h,sprite,number) -> None:
        """ Objet ne laissant passer qu'un personnage spécifique """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.number = number # numéro du personnage qui peut passer

    def draw(self,window):
        """ Dessine la porte 
        Entrée : fenêtre 
        Sortie : Aucune """
        window.blit(self.sprite,self.rect)

class Platform():
    def __init__(self,x,y,l,h,sprite) -> None:
        """ Simple plateforme ; fait office de mur """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite

    def draw(self,window):
        """ Dessine la plateforme
        Entrée : fenêtre 
        Sortie : Aucune """
        #pygame.draw.rect(window,self.color,self.rect)
        window.blit(self.sprite,self.rect)

class End():
    def __init__(self,x,y,l,h,sprite) -> None:
        """ Simple plateforme ; fait office de mur """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite

    def draw(self,window):
        """ Dessine la plateforme
        Entrée : fenêtre 
        Sortie : Aucune """
        #pygame.draw.rect(window,self.color,self.rect)
        window.blit(self.sprite,self.rect)

class Stage():
    def __init__(self,platforms,swaps,doors,end) -> None:
        """ Stage ; contient tous les éléments du niveau (plateformes, portes, swaps) """
        self.platforms = platforms
        self.swaps = swaps
        self.doors = doors
        self.end = end
    
    def draw(self,window):
        """ Dessine les éléments du stage
        Entrée : fenêtre 
        Sortie : Aucune """
        for p in self.platforms :
            p.draw(window)
        for s in self.swaps :
            s.draw(window)
        for d in self.doors :
            d.draw(window)
        for e in self.end :
            e.draw(window)