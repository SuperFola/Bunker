from .utils import *
import time


class ProcessManager:
    instance = None

    def __init__(self):
        if not ProcessManager.instance or ProcessManager.instance != self:
            ProcessManager.instance = self
        self._windows = []
        self._adding_order = []
        self._clock = pygame.time.Clock()
        self._execution_datas = {}

    @staticmethod
    def update_process(process):
        start = time.time()
        process.update()
        ProcessManager.instance._execution_datas[id(process)]['exc_times'].append(time.time() - start)

    @staticmethod
    def clock():
        return ProcessManager.instance._clock

    @staticmethod
    def windows():
        return ProcessManager.instance._windows

    @staticmethod
    def windows_ordered_by_date():
        return ProcessManager.instance._adding_order

    @staticmethod
    def add_windows(*news):
        for new in news:
            ProcessManager.windows().append(new)
            ProcessManager.windows_ordered_by_date().append(new)

            ProcessManager.instance._execution_datas[id(new)] = {
                'exc_times': []
            }

    @staticmethod
    def get_sizeof_window(index):
        if 0 <= index < len(ProcessManager.windows()):
            return ProcessManager.windows().__sizeof__()
        raise IndexError("Can not acces window at '%i'" % index)

    @staticmethod
    def init_windows_with(*args):
        for i, window in enumerate(ProcessManager.windows()):
            ProcessManager.windows()[i] = window(*args)

    @staticmethod
    def reoder_ifalive():
        alives = []
        not_alives = []
        for w in ProcessManager.windows():
            if w.alive():
                alives.append(w)
            else:
                not_alives.append(w)
        ProcessManager.instance._windows = alives + not_alives
