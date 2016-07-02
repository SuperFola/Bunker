from . utils import *
from . import bad_2048
from glob import glob
import os


class Connect:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.files = {}
        self.done = False
        self.connected = False
        self.user_pwd = ""
        self.session = "user"
        self.session_text = font.render(self.session, 1, BLACK)
        self.text = font.render("", 1, WHITE)
        self.max_len_pwd = 20
        self.quitter = font.render("Quitter", 1, BLACK)
        self.wrong = font.render("WRONG", 1, BLACK)
        self.pos_text_box = ((self.screen.get_width() - 200) // 2, (self.screen.get_height() - 20) // 2)
        self.error_box_pos = ((self.screen.get_width() - 225) // 2, (self.screen.get_height() - 150) // 2)
        self.wrong_pos = ((self.screen.get_width() - self.wrong.get_width()) // 2, (self.screen.get_height() - self.wrong.get_height()) // 2)
        self.avatar_pos = ((self.screen.get_width() - 200) // 2, (self.screen.get_height() - 200) // 2 - 200)
        self.user_pos = ((self.screen.get_width() - self.session_text.get_width()) // 2, (self.screen.get_height() - self.session_text.get_height()) // 2 - 50)
        try:
            self.password = eval(open("system/datas/pwd.bad").read())
        except SyntaxError:
            print("Password corrupted. Can not continue.")
            self.done = True
            self.connected = False

    def load(self):
        for file in glob("system/resx/connect/*.png"):
            self.files[os.path.basename(file).split('.')[0]] = pygame.image.load(file).convert_alpha()
            if os.path.basename(file).split('.')[0] in self.password.keys():
                self.files[os.path.basename(file).split('.')[0]] = pygame.transform.scale(self.files[os.path.basename(file).split('.')[0]], (200, 200))

    def _check(self):
        if bad_2048.crypt(4, self.user_pwd) == self.password[self.session]:
            self.connected = True
        else:
            self.user_pwd = ""
            self._error()

    def _error(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == KEYDOWN and ev.key == K_RETURN:
                break

            pygame.draw.rect(self.screen, RED, self.error_box_pos + (255, 150))
            self.screen.blit(self.wrong, self.wrong_pos)

            pygame.display.flip()

    def _change_session(self, new):
        if new in self.password.keys():
            self.session = new
            self.user_pos = ((self.screen.get_width() - self.session_text.get_width()) // 2, (self.screen.get_height() - self.session_text.get_height()) // 2 - 50)
        else:
            self._error()

    def run(self):
        self.load()

        while not self.done:
            pygame.draw.rect(self.screen, PASTEL_BLUE, (0, 0) + self.screen.get_size())
            pygame.draw.rect(self.screen, PASTEL_ORANGE, (4 * self.screen.get_width() / 5, 0, self.screen.get_width() / 5, self.screen.get_height()))

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.done = False
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self._check()
                    elif event.key == K_BACKSPACE:
                        self.user_pwd = self.user_pwd[:-1]
                    else:
                        if len(self.user_pwd) < self.max_len_pwd:
                            self.user_pwd += event.unicode
                    self.text = font.render("*" * len(self.user_pwd), 1, WHITE)

            self.screen.blit(self.quitter, (0, self.screen.get_height() - self.quitter.get_height()))
            pygame.draw.rect(self.screen, BLACK, self.pos_text_box + (200, 20))
            self.screen.blit(self.text, ((self.screen.get_width() - self.text.get_width()) // 2, (self.screen.get_height() - self.text.get_height()) // 2 + 5))
            self.screen.blit(self.files[self.session], self.avatar_pos)
            self.screen.blit(self.session_text, self.user_pos)

            pygame.display.flip()
