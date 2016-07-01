import pygame
import system
import apps


pygame.init()

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

win_manager = system.wm.DesktopManager(win)

win_manager.add_windows(*system.app_list, *apps.app_list)
win_manager.run()

pygame.quit()
