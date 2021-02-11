from AutoLab.widgets.wrapper_widgets import AutolabTimer
from PyQt5.QtCore import QObject, QTimerEvent


class AutolabCountTimer(AutolabTimer):
    def __init__(self, parent: QObject) -> None:
        super().__init__(parent)
        self._counter = 0
        self._enable_counter = True

    @property
    def counter(self) -> int:
        return self._counter

    @counter.setter
    def counter(self, count: int) -> None:
        self._counter = count

    @property
    def enable_counter(self) -> bool:
        return self._enable_counter

    @enable_counter.setter
    def enable_counter(self, enable: bool) -> None:
        self._enable_counter = enable

    def _increment(self) -> None:
        if self._enable_counter:
            self._counter += 1
        else:
            pass

    def stop(self) -> None:
        super().stop()
        self._counter = 0

    def timerEvent(self, a0: QTimerEvent) -> None:
        self._increment()
        return super().timerEvent(a0)
