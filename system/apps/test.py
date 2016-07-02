from . import Window
from ..utils import *


class App(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="FPS",
            version=1.0,
            pos=(50, 80),
            size=(100, 400),
            couleur=WHITE
        )

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

        self._content.blit(font.render(str(int(ProcessManager.clock().get_fps())), 1, BLACK), (0, 0))

    def trigger_user(self, event):
        pass
