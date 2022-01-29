import pygame
from Stage import Stage
from functions import signe
from copy import deepcopy

class Player():
    def __init__(self,x,y,l,h,color,number) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color
        self.vx = 0
        self.vy = 0
        self.grounded = False
        self.canwalljump = 0
        self.swapping = False
        self.must_swap = False
        self.number = number
    
    def move(self,left:bool,right:bool,up:bool,stage:Stage,other):
        """ Déplace le personnage, et effectue toutes les modifications nécessaires 
        entrées : left/right/up : inputs des touches directionnelles  ;  stage : stage en cours
        """
        # Création de la liste des objets à collisions
        detect = [p for p in stage.platforms] + [other]
        for d in stage.doors :
            if d.number != self.number :
                detect.append(d)
        # Inversion
        self.swap(stage.swaps)

        # Déplacement
        self.calculate_next_frame(detect,other)
        self.rect = self.rect.move(self.vx,self.vy)

        # Empêche de cheat en appuyant sur gauche ET droite eheh
        if left and right :
            left = False
            right = False
        
        # Gravité et décélération
        if self.grounded :
            self.vy = 0
        else :
            self.vy += 0.3
        self.vx *= 0.85

        # déplacement clavier
        if left :
            self.vx -= 0.6
        if right :
            self.vx += 0.6
        if up :
            if self.grounded :
                self.vy = -5
            # walljumps
            elif self.canwalljump < 0 and right :
                self.vy = -4
                self.vx = -4 * self.canwalljump
            elif self.canwalljump > 0 and left :
                self.vy = -4
                self.vx = -4 * self.canwalljump


    def calculate_next_frame(self,detect,other):
        """ Calcule la position de la frame suivante, évite de rentrer dans un mur
        calcule si le personnage est au sol et s'il peut walljump
        Entrée : liste des éléments à collisions
        Sortie : Aucune
        """
        self.grounded = False
        self.canwalljump = 0

        # détection des collisions
        for platform in detect :
            # collisions horizontales
            nextframe = self.rect.move(self.vx+signe(self.vx),-signe(self.vy))
            if nextframe.colliderect(platform.rect):
                i = 0
                previousrect = deepcopy(self.rect)
                while (not self.rect.move(signe(self.vx),-signe(self.vy)).colliderect(platform.rect)) and i <= (abs(self.vx)+1)*3:
                    self.rect.x += signe(self.vx)
                    i += 1
                if i > (abs(self.vx)+1)*3 :
                    self.rect = previousrect
                self.rect.x -= signe(self.vx)
                self.vx = 0
            
            # collisions verticales
            nextframe = self.rect.move(signe(self.vx),self.vy)
            if nextframe.colliderect(platform.rect):
                i = 0
                previousrect = deepcopy(self.rect)
                while (not self.rect.move(0,signe(self.vy)).colliderect(platform.rect)) and i <= (abs(self.vy)+1)*3:
                    self.rect.y += signe(self.vy)
                    i += 1
                if i > (abs(self.vy)+1)*3 :
                    self.rect = previousrect
                else :
                    self.vy = 0

            # percute le plafond
            if self.rect.move(0,-1).colliderect(platform) and not platform == other:
                self.vy = 2
            # grounded
            if self.rect.move(0,1).colliderect(platform):
                self.grounded = True
            
            # peut walljump
            if self.rect.move(2,-1).colliderect(platform):
                self.canwalljump = 1
            if self.rect.move(-2,-1).colliderect(platform):
                if self.canwalljump == 1 : # ne peut pas walljump DANS un mur
                    self.canwalljump = 0
                else:
                    self.canwalljump = -1

    def swap(self,swaps):
        """ Détecte si le personnage touche un élément faisant swap les joueurs 
        Entrée : liste des swaps
        Sortie : Aucune
        """
        self.must_swap = False
        # Touche-t-on un swap
        for swap in swaps :
            if self.rect.colliderect(swap.rect):
                self.must_swap = True
        # Empêche le swap infini
        if not self.must_swap :
            self.swapping = False
        if self.swapping :
            self.must_swap = False

    def draw(self,window):
        """ Dessine le personnage 
        Entrée : fenêtre 
        Sortie : Aucune """
        pygame.draw.rect(window,self.color,self.rect)