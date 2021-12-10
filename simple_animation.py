# Simple Animation with PyGame, Azehreya Franklin, 12/10/21, 1:06PM, v0.3

import pygame, sys, time
from pygame.locals import *

from myFirstPygame import GREEN, RED, WHITE

# Setup PyGame
pygame.init()

# Setup the window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction Variables. 
DOWNLEFT = "downleft"
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Set up color values 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)