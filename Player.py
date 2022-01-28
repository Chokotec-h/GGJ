from sys import platform
import pygame
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
    
    def move(self,left:bool,right:bool,up:bool,platforms:list,swaps:list,doors:list):
        detect = [p for p in platforms]
        for d in doors :
            if d.number != self.number :
                detect.append(d)
        self.calculate_next_frame(detect)
        self.swap(swaps)
        self.rect = self.rect.move(self.vx,self.vy)


        if left and right :
            left = False
            right = False
        
        if self.grounded :
            self.vy = 0
        else :
            self.vy += 0.3
        self.vx *= 0.85

        if left :
            self.vx -= 0.6
        if right :
            self.vx += 0.6
        if up :
            if self.grounded :
                self.vy = -5
            elif self.canwalljump < 0 and right :
                self.vy = -4
                self.vx = -4 * self.canwalljump
            elif self.canwalljump > 0 and left :
                self.vy = -4
                self.vx = -4 * self.canwalljump


    def calculate_next_frame(self,platforms):
        self.grounded = False
        self.canwalljump = 0

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
            if self.rect.move(0,-1).colliderect(platform):
                self.vy = 2
            
            if self.rect.move(2,-1).colliderect(platform):
                self.canwalljump = 1
            if self.rect.move(-2,-1).colliderect(platform):
                if self.canwalljump == 1 :
                    self.canwalljump = 0
                else:
                    self.canwalljump = -1

    def swap(self,swaps):
        self.must_swap = False
        for swap in swaps :
            if self.rect.colliderect(swap.rect):
                self.must_swap = True
        if not self.must_swap :
            self.swapping = False
        if self.swapping :
            self.must_swap = False

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)