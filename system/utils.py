import pygame
from pygame.locals import *
from enum import Enum


class WStates(Enum):
    def __init__(self, state):
        self.state = state

    ACTIVE = 0
    UNACTIVE = 1
    NOT_RESPONDING = 2
    WAITING = 3


RED = (180, 20, 20)
GREEN = (20, 180, 20)
BLUE = (20, 20, 180)
YELLOW = (20, 180, 180)
PURPLE = (180, 20, 180)
WHITE = (255, 255, 255)
GREY = (140, 140, 140)
BLACK = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font("system/resx/freesansbold.ttf", 16)
font_petite = pygame.font.Font("system/resx/freesansbold.ttf", 11)
