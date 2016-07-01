#-*-coding:Utf-8-*-

import time
from .utils import *
from . import process_manager


class DesktopManager:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.tskb_size = (120, self.screen.get_height())
        self.cl_tskb = GREEN
        self.main_txt_tsk_bar = pygame.image.load("system/resx/logo.png")
        self._content = pygame.Surface((self.screen.get_width() - self.tskb_size[0], self.screen.get_height()))

    def update(self):
        process_manager.ProcessManager.reoder_ifalive()
        self.draw()
        pygame.display.flip()

    # TODO: prévoir un écran de connexion
    def on_start(self):
        process_manager.ProcessManager.init_windows_with(self._content)
        w, h = self.main_txt_tsk_bar.get_size()
        self.main_txt_tsk_bar = pygame.transform.scale(self.main_txt_tsk_bar,
            (self.tskb_size[0], int(self.tskb_size[0] / w * h))
        )

    # TODO: prévoir un écran de déconnexion
    def on_end(self):
        pass

    def run(self):
        self.on_start()

        while not self.done:
            ProcessManager.clock().tick()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.done = True
                else:
                    self.trigger(event)
            self.update()

        self.on_end()

    def draw(self):
        pygame.draw.rect(self._content, BLACK, (0, 0) + self._content.get_size())

        for i in process_manager.ProcessManager.windows()[::-1]:
            i.draw()
        self.draw_task_bar()
        self.main_button_tsk_bar()
        self.print_time()
        self.screen.blit(self._content, (self.tskb_size[0], 0))

    def draw_task_bar(self):
        pygame.draw.rect(self.screen, self.cl_tskb, (0, 0) + self.tskb_size)
        y = self.main_txt_tsk_bar.get_height() + 10
        dispo = (self.tskb_size[0] - 8) // 6
        color = RED
        for i in process_manager.ProcessManager.windows():
            if i.state == WStates.ACTIVE:
                color = WHITE
            elif i.state == WStates.UNACTIVE:
                color = BLACK
            elif i.state == WStates.NOT_RESPONDING:
                color = BLUE
            elif i.state == WStates.WAITING:
                color = YELLOW
            txt = font_petite.render(i.get_title()[:dispo], 1, color)
            self.screen.blit(txt, (4, y))
            y += txt.get_height() + 4

    def main_button_tsk_bar(self):
        pygame.draw.rect(self.screen, YELLOW, (0, 0, self.tskb_size[0], self.main_txt_tsk_bar.get_height()))
        self.screen.blit(self.main_txt_tsk_bar, (0, 0))

    def select_prog(self, y=0):
        real_select = (y - self.main_txt_tsk_bar.get_height() - 10) // 14
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
