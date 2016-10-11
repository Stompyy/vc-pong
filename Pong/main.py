import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()  # Used for sounds

# Declare all variables etc
font = pygame.font.SysFont(None, 48)
playerOneScore = 0
playerTwoScore = 0

# Usual colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# window dimensions
windowHeight = 600
windowWidth = 800

# paddle dimensions
paddleHeight = 70
paddleWidth = 10

# ball variables
ballRadius = 10
ballX = 400.0
ballY = 300.0
ballMoveX = -0.1
ballMoveY = -0.1

#default player positions
playerOneX = 20     # constant for left hand side
playerOneY = 300.0  # variable sets to the middle, then value is changed with controls
                    # declared as float because int made movement too fast. have to convert to int later as position is
                    # int only.
playerTwoX = 780    # constant for right hand side
playerTwoY = 300.0  # variable sets to the middle, then value is changed with controls

window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)


class Paddle:
    def __init__(self, x, y):
        pygame.draw.rect(window, GREEN, (x, y, paddleWidth, paddleHeight))
        self.rect = pygame.Rect(x, y, paddleWidth, paddleHeight)    # creates collider


class Ball:
    def __init__(self, x, y):
        self.x = x  # Don't think that these do anything, but it gets angry when I delete them.
        self.y = y  # I probably reference them later
        pygame.draw.circle(window, GREEN, (int(ballX), int(ballY)), ballRadius)

        #  left collider below as rect. Don't need to do circle one and circle to rect collisions not as straightforward
        self.rect = pygame.Rect(int(ballX), int(ballY), ballRadius * 2, ballRadius * 2)  # creates collider


# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # player one controls
    if keys[pygame.K_w]:
        playerOneY += -0.1
    if keys[pygame.K_s]:
        playerOneY += 0.1

    # player two controls
    if keys[pygame.K_o]:
        playerTwoY += -0.1
    if keys[pygame.K_l]:
        playerTwoY += 0.1

    # setting limits to stop each paddle leaving the window area
    if playerOneY < 0:
        playerOneY = 0
    if playerOneY > windowHeight - paddleHeight:    # because it measures the paddle position from the top left of
        playerOneY = windowHeight - paddleHeight    # the rectangle so need to adjust for this
    if playerTwoY < 0:
        playerTwoY = 0
    if playerTwoY > windowHeight - paddleHeight:
        playerTwoY = windowHeight - paddleHeight

    window.fill(BLACK)  #for haxor l33t

    # move ball then draw it with the new coordinates
    ballX += ballMoveX
    ballY += ballMoveY
    ball = Ball(int(ballX), int(ballY))

    # bounce ball off top and bottom walls
    if ballY < 0 or ballY > windowHeight:
        ballMoveY *= -1

    # calling the class, so don't need to tell to draw, the .draw() command is it is in the classes __init__() function
    # just supplying the (x, y) coordinates. x is a constant, and each y is defined in the controls above
    playerOne = Paddle(playerOneX, int(playerOneY))
    playerTwo = Paddle(playerTwoX, int(playerTwoY))

    # check for paddle collision and bounce back if true
    if ball.rect.colliderect(playerOne.rect)or ball.rect.colliderect(playerTwo.rect):
        ballMoveX *= -1

    # if ball leaves left or right edges, reset ball position and add to score
    # be nice to make these random. Not now though
    if ball.x < 0:
        ballX = 400.0
        ballY = 300.0
        ballMoveX = -0.1
        ballMoveY = -0.1
        playerTwoScore += 1

    if ball.x > windowWidth:
        ballX = 400.0
        ballY = 300.0
        ballMoveX = -0.1
        ballMoveY = -0.1
        playerOneScore += 1

    # Display score
    playerOneText = font.render(('Player 1 : ' + str(playerOneScore)), True, GREEN)
    window.blit(playerOneText, (5, 10))

    playerTwoText = font.render(('Player 2 : ' + str(playerTwoScore)), True, GREEN)
    window.blit(playerTwoText, (580, 10))

    pygame.display.update()
