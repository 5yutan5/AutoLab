from PyQt5.QtCore import QObject, Qt, QTimer
from PyQt5.QtWidgets import QAction, QPushButton, QToolButton


class PushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(Qt.PointingHandCursor)


class ToolButton(QToolButton):
    def __init__(self):
        super().__init__()
        self.setCursor(Qt.PointingHandCursor)


class AutolabAction(QAction):
    """AutoLab QAction class wrapper to handle cross platform patches."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AutolabTimer(QTimer):
    """AutoLab QTimer class wrapper to handle cross platform patches."""

    def __init__(self, parent: QObject):
        super().__init__(parent=parent)


def test():
    import sys

    from AutoLab.utils.qthelpers import qapplication

    app = qapplication()
    push_button = PushButton("Test")
    push_button.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    test()
