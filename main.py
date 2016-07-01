import pygame
from bados import *


pygame.init()
win = pygame.display.set_mode((0, 0), FULLSCREEN)
win_manager = DesktopManager(win)
test = Window(win, "Test", 1.0, size=(540, 480), pos=(120, 120))
other = Window(win, "Another window", size=(200, 300), pos=(200, 160), couleur=(75, 40, 125))
win_manager.add_windows(test, other)
win_manager.run()
