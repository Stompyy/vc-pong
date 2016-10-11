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

ballRadius = 10

playerOneY = 200
playerOneSpawnd = False
playerTwoY = 200



window = pygame.display.set_mode((width, height), 0, 32)


ball = pygame.draw.circle(window, WHITE, (400, 400), ballRadius, 0)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
<<<<<<< HEAD
        self.image = pygame.draw.rect(window, GREEN, (150,10, 50, 20), 0)

=======
        self.image = pygame.draw.rect(window, GREEN,(100, 100),0)
       #penis
>>>>>>> 90bfe5f71e194f3325f043bbd355f6d9edd73b8a
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ball
    #     whasson


    def wallBounce(self, incomingY):
        self.y = - incomingY
        return self.y




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerOneY += -1
    if keys[pygame.K_s]:
        playerOneY += 1

    if playerOneSpawnd == False:
        playerOne = Paddle(20, 200)
        playerOneSpawnd = True

    window.fill(BLACK)

    pygame.draw.circle(window, WHITE, (400, playerOneY), ballRadius, 0)
    pygame.draw.rect(window, GREEN, (20, 150 + playerOneY, 10, 50), 0)


    pygame.display.update()
