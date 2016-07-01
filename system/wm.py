#-*-coding:Utf-8-*-

import time
from .utils import *
from . import process_manager


class DesktopManager:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.clock = pygame.time.Clock()
        self.tskb_size = (100, self.screen.get_height())
        self.cl_tskb = GREEN
        self.main_txt_tsk_bar = font.render("BunkerOS", 1, RED)
        self._content = pygame.Surface((self.screen.get_width() - self.tskb_size[0], self.screen.get_height()))

    def update(self):
        process_manager.ProcessManager.reoder_ifalive()

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

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0) + self.screen.get_size())

        for i in process_manager.ProcessManager.windows()[::-1]:
            i.draw()
        self.draw_task_bar()
        self.main_button_tsk_bar()
        self.print_fps()
        self.screen.blit(self._content, (self.tskb_size[0], 0))
        self.print_time()

    def draw_task_bar(self):
        pygame.draw.rect(self.screen, self.cl_tskb, (0, 0) + self.tskb_size)
        y = 40
        for i in process_manager.ProcessManager.windows():
            dispo = (self.tskb_size[0] - 8) // 6
            txt = font_petite.render(i.get_title()[:dispo], 1, WHITE if i in process_manager.ProcessManager.windows() else GREY)
            self.screen.blit(txt, (4, y))
            y += txt.get_size()[1] + 4

    def main_button_tsk_bar(self):
        pygame.draw.rect(self.screen, YELLOW, (0, 0, self.tskb_size[0], 30))
        self.screen.blit(self.main_txt_tsk_bar,
                ((self.tskb_size[0] - self.main_txt_tsk_bar.get_size()[0]) // 2,
                  self.main_txt_tsk_bar.get_size()[1] // 2))

    def print_fps(self):
        pygame.draw.rect(self.screen, GREY, (self.screen.get_width() - 50, 0, 90, 20))
        self.screen.blit(font.render(str(int(self.clock.get_fps())), 1, BLACK), (self.screen.get_width() - 40, 2))

    def select_prog(self, y=0):
        real_select = (y - 40) // 14
        print(y, real_select)
        if 0 <= real_select < len(process_manager.ProcessManager.windows()):
            if real_select < len(process_manager.ProcessManager.windows()):
                process_manager.ProcessManager.windows()[real_select].set_alive()

    def print_time(self):
        t = time.strftime("%A")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 42))
        t = time.strftime("%H : %M : %S")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 14))
        t = time.strftime("%d %B")
        self.screen.blit(font_petite.render(t, 1, WHITE), (4, self.screen.get_size()[1] - 28))

    def trigger(self, event):
        if event.type == MOUSEBUTTONDOWN and event.pos[0] > self.tskb_size[0] or event.type != MOUSEBUTTONDOWN:
            if event.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION):
                event.pos = (event.pos[0] - self.tskb_size[0], event.pos[1])
            if len(process_manager.ProcessManager.windows()) >= 1:
                process_manager.ProcessManager.windows()[0].trigger(event)
        elif event.type == MOUSEBUTTONDOWN and event.pos[0] <= self.tskb_size[0]:
            self.select_prog(event.pos[1])
