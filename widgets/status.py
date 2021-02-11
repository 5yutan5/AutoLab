from AutoLab.utils.system import cpu_usage, phymem_usage
from AutoLab.widgets.wrapper_widgets import ToolButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QAction, QStatusBar


class StatusBarWidget(ToolButton):
    def __init__(self, action: QAction, align: str, statusbar: QStatusBar):
        super().__init__()
        self._permanent_text = ""
        self._temporary_text = ""
        self.setDefaultAction(action)
        if align == "right":
            statusbar.addPermanentWidget(self)
        elif align == "left":
            statusbar.addWidget(self)

    def set_permanent_text(self, text: str):
        self._permanent_text = text
        self.setText(self._permanent_text + self._temporary_text)

    def set_temporary_text(self, text: str):
        self._temporary_text = text
        self.setText(self._permanent_text + self._temporary_text)


class BaseTimerStatus(StatusBarWidget):
    def __init__(self, action: QAction, align: str, statusbar: QStatusBar):
        super().__init__(action, align, statusbar)
        self._interval = 2000
        self._timer = QTimer()
        self._timer.timeout.connect(self.update_status)
        self._timer.start(self._interval)

    def update_status(self):
        self.set_temporary_text(self.get_text())

    def set_temporary_text(self, text: str):
        return super().set_temporary_text(text)

    def get_text(self) -> str:
        return ""


class MemoryStatus(BaseTimerStatus):
    """Status bar widget for system memory usage."""

    def __init__(self, action: QAction, align: str, statusbar: QStatusBar):
        super().__init__(action, align, statusbar)
        self.set_permanent_text("Mem: ")

    def get_text(self):
        """Return memory usage."""
        return f"{phymem_usage()}%"


class CPUStatus(BaseTimerStatus):
    """Status bar widget for system cpu usage."""

    def __init__(self, action: QAction, align: str, statusbar: QStatusBar):
        super().__init__(action, align, statusbar)
        self.set_permanent_text("CPU: ")

    def get_text(self):
        """Return cpu usage."""
        return f"{cpu_usage()}%"


def test():
    import sys

    from AutoLab.utils.qthelpers import qapplication
    from PyQt5.QtWidgets import QMainWindow

    def sample():
        print("hello")

    app = qapplication()
    win = QMainWindow()
    win.setWindowTitle("Test")
    win.resize(900, 300)
    statusbar = win.statusBar()
    statusbar.setContextMenuPolicy(Qt.ActionsContextMenu)
    action = QAction("test")
    action.triggered.connect(sample)
    MemoryStatus(action, statusbar)
    CPUStatus(action, statusbar)
    statusbar.addAction(action)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    test()
