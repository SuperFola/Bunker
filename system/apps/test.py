from . import Window
import pygame


class App(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="App System Test",
            version=1.0,
            pos=(50, 80),
            size=(100, 400),
            couleur=(20, 20, 20)
        )

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

        # on va tester le débordement
        pygame.draw.rect(self._content, (255, 0, 0), (20, 100, 350, 350))

    def trigger_user(self, event):
        pass
