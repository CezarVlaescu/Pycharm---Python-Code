import pygame
import os
import sys
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))
bg = pygame.image.load("cartoon-background-mountain-lake-free-video.jpg")
pygame.mouse.set_visible(False)
pygame.display.set_caption("CatchTheApples")

class Catch:
    def __init__(self, screenheight, screenwidth, imagefile):
        self.image = pygame.image.load(imagefile)
        self.top = screenheight - self.shape.get_height()
        self.left = screenwidth/2 - self.shape.get_width()/2

    def show(self, surface):
        surface.blit(self.shape, (self.top, self.left))

    def UpdateCoords(self, x):
        self.left = x - self.shape.get_width()/2


while True:

    # Calculate the frame rate of the game : 60 FPS
    clock.tick(60)
    screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()





