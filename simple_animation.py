# Simple Animation with PyGame, Azehreya Franklin, 12/10/21, 12:59PM, v0.2

import pygame, sys, time
from pygame.locals import *

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
