import pygame
import system
import apps


pygame.init()

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

win_manager = system.wm.DesktopManager(win)

test = system.window.Window(win, "Test", 1.0, size=(540, 480), pos=(120, 120))
other = system.window.Window(win, "Another window", size=(200, 300), pos=(200, 160), couleur=(75, 40, 125))

win_manager.add_windows(test, other, *apps.app_list)
win_manager.run()

pygame.quit()
