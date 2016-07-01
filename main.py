import pygame
import system
import apps


pygame.init()

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

win_manager = system.wm.DesktopManager(win)
system.process_manager.ProcessManager()

system.process_manager.ProcessManager.add_windows(*[_ for _ in system.app_list + apps.app_list])
system.process_manager.ProcessManager.init_windows_with(win)
win_manager.run()

pygame.quit()
