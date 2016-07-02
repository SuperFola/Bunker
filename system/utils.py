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


RED = (180, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 180)
YELLOW = (0, 180, 180)
PURPLE = (180, 0, 180)
ORANGE = (180, 180, 0)

WHITE = (255, 255, 255)
GREY = (156, 156, 156)
BLACK = (0, 0, 0)

PASTEL_BLUE = (40, 40, 150)
PASTEL_RED = (150, 40, 40)
PASTEL_GREEN = (40, 150, 40)
PASTEL_YELLOW = (40, 150, 150)
PASTEL_PURPLE = (150, 40, 150)
PASTEL_ORANGE = (150, 150, 40)

pygame.font.init()
font = pygame.font.Font("system/resx/freesansbold.ttf", 16)
font_petite = pygame.font.Font("system/resx/freesansbold.ttf", 11)
