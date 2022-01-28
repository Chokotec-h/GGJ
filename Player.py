from sys import platform
import pygame
from functions import signe
from copy import deepcopy

class Player():
    def __init__(self,x,y,l,h,color) -> None:
        self.rect = pygame.Rect(x,y,l,h)
        self.color = color
        self.vx = 0
        self.vy = 0
        self.grounded = False
    
    def move(self,left:bool,right:bool,up:bool,platforms:list):
        self.calculate_next_frame(platforms)
        self.rect = self.rect.move(self.vx,self.vy)
        
        if self.grounded :
            self.vy = 0
        else :
            self.vy += 0.5
        self.vx *= 0.5

        if left :
            self.vx -= 4
        if right :
            self.vx += 4
        if up and self.grounded :
            self.vy = -10


    def calculate_next_frame(self,platforms):
        self.grounded = False

        for platform in platforms :
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

            if self.rect.move(0,1).colliderect(platform):
                self.grounded = True

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)