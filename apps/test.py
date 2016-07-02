from . import Window
from system.utils import *


class App(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="App Test",
            version=1.0,
            pos=(180, 300),
            size=(400, 100),
            couleur=(20, 20, 20)
        )

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

        # on va tester le débordement
        pygame.draw.rect(self._content, (255, 255, 0), (100, 20, 350, 350))

    def trigger_user(self, event):
        pass

    def update(self):
        pass
