from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QSlider,
    QSpinBox,
    QTabWidget,
    QWidget,
)


class PathNameLine(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)

    def set_path(self, name: str):
        self.setText(name)
        self.setCursorPosition(0)


class PageTab(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tabBar().setDisabled(True)
        self.tabBar().hide()


class IntSlider(QWidget):
    def __init__(self):
        super().__init__()
        self._slider = QSlider(Qt.Horizontal)
        self._spinbox = QSpinBox()

        # setup signal
        self._slider.valueChanged.connect(self._slot_value_changed)
        self._spinbox.valueChanged.connect(self._slot_value_changed)

        # setup layout
        h_layout = QHBoxLayout(self)
        h_layout.addWidget(self._slider)
        h_layout.addWidget(self._spinbox)

    @pyqtSlot(int)
    def _slot_value_changed(self, value: int) -> None:
        sender = self.sender()
        if sender is self._slider:
            self._spinbox.blockSignals(True)
            self._spinbox.setValue(value)
            self._spinbox.blockSignals(False)
        elif sender is self._spinbox:
            self._slider.blockSignals(True)
            self._slider.setValue(value)
            self._slider.blockSignals(False)

    def get_value(self) -> int:
        return self._spinbox.value()

    def set_range(self, min: int, max: int) -> None:
        self._slider.setRange(min, max)
        self._spinbox.setRange(min, max)

    def set_current_value(self, val: int) -> None:
        self._spinbox.setValue(val)


def test():
    import sys

    from AutoLab.utils.qthelpers import qapplication

    app = qapplication()
    file_name_line = PathNameLine()
    file_name_line.show()
    int_slider = IntSlider()
    int_slider.set_range(1, 10)
    int_slider.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    test()
