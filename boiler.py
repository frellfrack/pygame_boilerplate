#!/usr/bin/python3
import pygame
from math import pi,sin,cos
from time import sleep

class pygameBoilerPolate:
    def __init__(self,options):

        self.defaults={
        "width":800,
        "height":600
        }
        
        self.options = {**self.defaults,**options}
        
        #self.printFonts()
        pygame.init()
        self.width=self.options["width"]
        self.height=self.options["height"]
        size = [self.width, self.height]
        self.screen = pygame.display.set_mode(size)
        self.centreX = self.width/2
        self.centreY = self.height/2
        self.clock = pygame.time.Clock()
        self.done=False
        pygame.display.set_caption(self.options["title"])
        self.background=(0,0,0)
        self.labelColour=(255,255,255) 
        self.i=0
        self.mainLoop()
        
    def mainLoop(self):
        while not self.done:
            self.getEvents()
            self.clock.tick()
            self.screen.fill(self.background)
            self.doStuff()
            pygame.display.flip()
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.done=True 
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q):
                    self.done=True
                elif (event.key == pygame.K_UP):
                    self.K_UP=True
                elif (event.key == pygame.K_DOWN):
                    self.K_DOWN=True
                elif (event.key == pygame.K_LEFT):
                    self.K_LEFT=True
                elif (event.key == pygame.K_RIGHT):
                    self.K_RIGHT=True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP):
                    self.K_UP=False
                elif (event.key == pygame.K_DOWN):
                    self.K_DOWN=False
                elif (event.key == pygame.K_LEFT):
                    self.K_LEFT=False
                elif (event.key == pygame.K_RIGHT):
                    self.K_RIGHT=False

    def drawLabel (self,cords,message,fontsize):
        font = pygame.font.SysFont(None, fontsize)
        text = font.render(message, True, self.labelColour)
        self.screen.blit(text,(cords[0]-text.get_width()/2, cords[1]-text.get_height()/2))

    def doStuff(self):
        self.i=self.i+1
        self.drawLabel([self.centreX,self.centreY],"I do nothing!",20) 
    def printFonts(self):
        fonts = pygame.font.get_fonts()
        print(len(fonts))
        for f in fonts:
            print(f)
    
if __name__ == "__main__":
    tmp =  pygameBoilerPolate({
    "width":800,
    "height":600,
    "title":"I Do Nothing",
    "background":(0,0,0),
    "labelColour":(255,255,255),
    })
