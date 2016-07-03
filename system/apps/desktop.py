# -*- coding: utf-8 -*-

from . import Window
from ..utils import *


class ProcessManagerWindow(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="Desktop",
            version=1.0,
            pos=(50, 50),
            size=(300, 500)
        )

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

    def trigger_user(self, event):
        pass
