import pygame

def signe(val):
    if val < 0 :
        return -1
    elif val > 0 :
        return 1
    else :
        return 0

def swap_chars(p1,p2):
    p1,p2 = p2,p1
    p1.vx,p2.vx = p2.vx,p1.vx
    p1.vy,p2.vy = p2.vy,p1.vy
    p1.sprite,p2.sprite = p2.sprite,p1.sprite
    p1.number,p2.number = p2.number,p1.number

    return p1,p2

def fadein(time):
    fadeout = pygame.Surface((800, 600))
    fadeout = fadeout.convert()
    fadeout.fill((0,0,0))
    fadeout.set_alpha(time)
    return fadeout

def fadeout(time):
    fadeout = pygame.Surface((800, 600))
    fadeout = fadeout.convert()
    fadeout.fill((0,0,0))
    fadeout.set_alpha(255-time)
    return fadeout