import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# Declare all variables etc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

height = 600
width = 800

window = pygame.display.set_mode((width, height), 0, 32)


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.draw.rect(window, GREEN,(100, 100),0)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wallBounce(self, incomingY):
        self.y = - incomingY
        return self.y


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
