from .utils import *


class Window:
    def __init__(self, screen, titre="", version=1.0, pos=(0, 0), size=(0, 0), couleur=(20, 20, 20), cote_c=12):
        self.screen = screen
        self.wscreen, self.hscreen = self.screen.get_size()
        self.titre = titre
        self.version = version
        self.fen_name = "[" + self.titre + "]" + " " + str(self.version)
        self.pos = pos
        self.size = size
        self.couleur = couleur
        self.cote_c = cote_c
        self.state = WStates.ACTIVE
        self.escape_btn = (
            self.pos[0] + self.size[0] - (24 - self.cote_c) // 2 - self.cote_c,
            self.pos[1] + (24 - self.cote_c) // 2,
            self.cote_c,
            self.cote_c
        )
        self._content = pygame.Surface(self.size)
        self.clic_on_barre = False

        self._blurw = pygame.Surface(self.size)
        self._blurw.fill(WHITE)
        self._blurw.convert_alpha()
        self._blurw.set_alpha(225)

    def draw_vitals(self):
        # barre
        pygame.draw.rect(self.screen, GREY, self.pos + (self.size[0], 24))
        # titre
        self.screen.blit(font.render(self.fen_name, 1, BLACK), (self.pos[0] + 2, self.pos[1] + 2))
        # croix
        pygame.draw.rect(self.screen, RED, self.escape_btn)

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

    def draw(self):
        if self.alive():
            self.draw_vitals()
            self.draw_content()
            if self.state == WStates.NOT_RESPONDING:
                self._content.blit(self._blurw, (0, 0))
            self.screen.blit(self._content, (self.pos[0], self.pos[1] + 24))

    def set_alive(self, value=WStates.ACTIVE):
        self.state = value

    def alive(self):
        return self.state in (WStates.ACTIVE, WStates.NOT_RESPONDING, WStates.WAITING)

    def get_title(self):
        return self.fen_name

    def trigger_vitals(self, event):
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.pos[0] <= x <= self.pos[0] + self.size[0] and self.pos[1] <= y <= self.pos[1] + 24:
                self.clic_on_barre = True
        if event.type == MOUSEMOTION:
            if self.clic_on_barre:
                pass
        if event.type == MOUSEBUTTONUP:
            x, y = event.pos
            if self.escape_btn[0] <= x <= self.escape_btn[0] + self.escape_btn[2] \
                    and self.escape_btn[1] <= y <= self.escape_btn[1] + self.escape_btn[3]:
                pygame.draw.rect(self.screen, BLACK, (0, 0) + self.screen.get_size())
                self.state = WStates.UNACTIVE

    def trigger_user(self, event):
        pass

    def trigger(self, event):
        self.trigger_vitals(event)
        self.trigger_user(event)
