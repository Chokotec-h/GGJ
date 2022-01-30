import pygame

class Swap():
    def __init__(self,x,y,l,h,sprite,hide) -> None:
        """ Objet inversant la position des deux personnages """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.show = not hide

    def draw(self,window):
        """ Dessine le swap 
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show :
            window.blit(self.sprite,self.rect)

class Door():
    def __init__(self,x,y,l,h,sprite,number,hide) -> None:
        """ Objet ne laissant passer qu'un personnage spécifique """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.number = number # numéro du personnage qui peut passer
        self.show = not hide

    def draw(self,window):
        """ Dessine la porte 
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show :
            window.blit(self.sprite,self.rect)

class Platform():
    def __init__(self,x,y,l,h,sprite,hide) -> None:
        """ Simple plateforme ; fait office de mur """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.show = not hide

    def draw(self,window):
        """ Dessine la plateforme
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show :
            window.blit(self.sprite,self.rect)

class End():
    def __init__(self,x,y,l,h,sprite,hide) -> None:
        """ Arrivée """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.show = not hide

    def draw(self,window):
        """ Dessine l'arrivée
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show :
            window.blit(self.sprite,self.rect)

class Secret_Cookie():
    def __init__(self,x,y,l,h,sprite,hide) -> None:
        """ Cookie caché eheheh """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.got = False
        self.show = not hide

    def draw(self,window):
        """ Dessine le magnifique cookie
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show and not self.got :
            window.blit(self.sprite,self.rect)

class Background():
    def __init__(self,x,y,l,h,sprite,hide) -> None:
        """ Arrière plan """
        self.rect = pygame.Rect(x,y,l,h)
        self.sprite = sprite
        self.show = not hide

    def draw(self,window):
        """ Dessine l'arrière plan
        Entrée : fenêtre 
        Sortie : Aucune """
        if self.show :
            window.blit(self.sprite,self.rect)

class Stage():
    def __init__(self,platforms,swaps,doors,end,cookies) -> None:
        """ Stage ; contient tous les éléments du niveau (plateformes, portes, swaps, arrivée, cookies secrets, background) """
        self.platforms = platforms
        self.swaps = swaps
        self.doors = doors
        self.end = end
        self.cookies = cookies
        self.background = []
        self.animations = []
    
    def draw(self,window):
        """ Dessine les éléments du stage
        Entrée : fenêtre 
        Sortie : Aucune """
        for b in self.background :
            b.draw(window)
        for p in self.platforms :
            p.draw(window)
        for s in self.swaps :
            s.draw(window)
        for d in self.doors :
            d.draw(window)
        for e in self.end :
            e.draw(window)
        for c in self.cookies :
            c.draw(window)