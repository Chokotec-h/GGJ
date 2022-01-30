import pygame

class Texte:
    def __init__(self,text,sysfont,color,x,y,l,show=True,format_ = "center"):
        self.x = x
        self.y = y
        self.show = show
        ratio = l/800

        sysfont = [sysfont[i] for i in range(len(sysfont))]
        sysfont[1] = round(sysfont[1] * ratio)
        self.font = pygame.font.SysFont(sysfont[0],sysfont[1], bold = sysfont[2], italic = sysfont[3])
        self.text= text
        self.color = color
        self.format = format_


    def draw(self,win,alpha):
        text = self.font.render(self.text,1,self.color)
        text.set_alpha(alpha)
        self.width = text.get_size()[0]
        self.height = text.get_size()[1]
        if self.format == "center":
            win.blit(text,(self.x - self.width//2 , self.y - self.height//2))
        elif self.format == "left":
            win.blit(text,(self.x , self.y - self.height//2))
        elif self.format == "right":
            win.blit(text,(self.x - self.width , self.y - self.height//2))
        else :
            win.blit(text,(self.x , self.y))