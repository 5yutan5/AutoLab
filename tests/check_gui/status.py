import sys

from AutoLab.utils.icon_manager import IconNames, create_qicon
from AutoLab.widgets.status import (
    CPUStatus,
    DeviceConnectStatus,
    MeasureStatus,
    MemoryStatus,
    StatusBar,
    StatusBarWidget,
)
from PySide6.QtWidgets import QApplication, QMainWindow


def statusbar():
    app = QApplication([])
    win = QMainWindow()
    win.setWindowTitle("Test")
    win.resize(900, 300)
    statusbar = StatusBar(win)
    statusbar.add_status(CPUStatus(), statusbar.Align.LEFT)
    statusbar.add_status(MemoryStatus(), statusbar.Align.LEFT)
    status_widget1 = StatusBarWidget("Status1")
    status_widget1.update_icon(create_qicon(IconNames.ADD_BEHAVIOR))
    status_widget1.sig_clicked.connect(lambda: print("Status1"))  # type: ignore
    statusbar.add_status(status_widget1)
    status_widget2 = StatusBarWidget("Status2")
    status_widget2.update_icon(create_qicon(IconNames.CONNECT))
    status_widget2.sig_clicked.connect(lambda: print("Status2"))  # type: ignore
    statusbar.add_status(status_widget2)
    statusbar.add_status(MeasureStatus())
    statusbar.add_status(DeviceConnectStatus("Stage Controller"))
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    statusbar()
