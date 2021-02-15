import functools

from PySide6.QtWidgets import QApplication


def qtapp_test(func):
    @functools.wraps(func)
    def wrapper():
        if QApplication.instance() is None:
            QApplication([])
        else:
            QApplication.instance()
        func()

    return wrapper
