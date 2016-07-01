#-*-coding:Utf-8-*-

import time
import pygame
from pygame.locals import *
from utils import *


pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 16)
font_petite = pygame.font.Font("freesansbold.ttf", 11)


class DesktopManager:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.clock = pygame.time.Clock()
        self.windows = []
        self.tskb_size = (100, self.screen.get_size()[1])
        self.cl_tskb = (45, 167, 37)
        self.main_txt_tsk_bar = font.render("BunkerOS", 1, RED)

    def update(self):
        alives = []
        not_alives = []
        for w in self.windows:
            if w.alive():
                alives.append(w)
            else:
                not_alives.append(w)
        self.windows = alives + not_alives

    def run(self):
        while not self.done:
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.done = True
                else:
                    self.trigger(event)
            self.draw()
            self.update()
            pygame.display.flip()

    def add_windows(self, *news):
        for new in news:
            self.windows.append(new)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0) + self.screen.get_size())

        for i in self.windows[::-1]:
            i.draw()
        self.draw_task_bar()
        self.main_button_tsk_bar()
        self.print_fps()
        self.print_time()

    def draw_task_bar(self):
        pygame.draw.rect(self.screen, self.cl_tskb, (0, 0) + self.tskb_size)
        y = 40
        for i in self.windows:
            dispo = (self.tskb_size[0] - 8) // 6
            txt = font_petite.render(i.get_title()[:dispo], 1, WHITE if i in self.windows else GREY)
            self.screen.blit(txt, (4, y))
            y += txt.get_size()[1] + 4

    def main_button_tsk_bar(self):
        pygame.draw.rect(self.screen, YELLOW, (0, 0, self.tskb_size[0], 30))
        self.screen.blit(self.main_txt_tsk_bar,
                ((self.tskb_size[0] - self.main_txt_tsk_bar.get_size()[0]) // 2,
                  self.main_txt_tsk_bar.get_size()[1] // 2))

    def print_fps(self):
        pygame.draw.rect(self.screen, GREY, (self.screen.get_width() - 50, 0, 90, 20))
        self.screen.blit(font.render(str(int(self.clock.get_fps())), 1, (10, 10, 10)), (self.screen.get_width() - 40, 2))

    def select_prog(self, y=0):
        real_select = (y - 40) // 14
        print(y, real_select)
        if 0 <= real_select < len(self.windows):
            if real_select < len(self.windows):
                self.windows[real_select].set_alive()

    def print_time(self):
        t = time.strftime("%A")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 42))
        t = time.strftime("%H : %M : %S")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 14))
        t = time.strftime("%d %B")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 28))

    def trigger(self, event):
        if event.type == MOUSEBUTTONDOWN and event.pos[0] > self.tskb_size[0] or event.type != MOUSEBUTTONDOWN:
            if len(self.windows) >= 1:
                self.windows[0].trigger(event)
        elif event.type == MOUSEBUTTONDOWN and event.pos[0] <= self.tskb_size[0]:
            self.select_prog(event.pos[1])


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
        self.living = True
        self.escape_btn = (
            self.pos[0] + self.size[0] - (24 - self.cote_c) // 2 - self.cote_c,
            self.pos[1] + (24 - self.cote_c) // 2,
            self.cote_c,
            self.cote_c
        )
        self.clic_on_barre = False

    def draw(self):
        if self.living:
            pygame.draw.rect(self.screen, self.couleur, self.pos + self.size)
            pygame.draw.rect(self.screen, (150, 150, 150), self.pos + (self.size[0], 24))
            self.screen.blit(font.render(self.fen_name, 1, (10, 10, 10)), (self.pos[0] + 2, self.pos[1] + 2))
            pygame.draw.rect(self.screen, RED, self.escape_btn)

    def set_alive(self, value=True):
        self.living = True

    def alive(self):
        return self.living

    def get_title(self):
        return self.fen_name

    def trigger(self, event):
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
                pygame.draw.rect(self.screen, (0, 0, 0), (0, 0) + self.screen.get_size())
                self.living = False
