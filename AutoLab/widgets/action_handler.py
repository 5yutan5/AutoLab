from typing import Type

from AutoLab.utils.icon_manager import IconName, icon
from AutoLab.widgets.status import StatusBarWidget
from AutoLab.widgets.wrapper_widgets import AutolabAction
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtWidgets import (QAction, QMainWindow, QMenu, QStatusBar, QToolBar,
                             QWidget)


class CheckMenu(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.check_icon = icon(IconName.CHECK_MARK)

    def set_visible_dict(self, dic: dict[str, int]):
        for name, isCheck in dic.items():
            self.addAction(self.check_icon, name) if isCheck else self.addAction(name)


class StatusBar(QStatusBar):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent=parent)
        self._visible_dict = {}
        self._widget_dict = {}
        parent.setStatusBar(self)

    def contextMenuEvent(self, event: QContextMenuEvent):
        menu = CheckMenu(self)
        menu.set_visible_dict(self._visible_dict)
        selected_action = menu.exec(self.mapToGlobal(event.pos()))
        if selected_action is not None:
            action_text = selected_action.text()
            is_check = self._visible_dict[action_text]
            self._visible_dict[action_text] = Qt.Unchecked if is_check else Qt.Checked
            if is_check:
                self._widget_dict[action_text].hide()
            else:
                self._widget_dict[action_text].show()

    def add_status(
        self,
        action: AutolabAction,
        status: Type[StatusBarWidget] = None,
        align: str = "right",
    ):
        super().addAction(action)
        widget = (
            StatusBarWidget(action, align, self)
            if status is None
            else status(action, align, self)
        )
        self._visible_dict[action.objectName()] = Qt.Checked
        self._widget_dict[action.objectName()] = widget

    def popup_actions(self, actions: list[QAction]):
        menu = QMenu()
        menu.addActions(actions)
        menu.adjustSize()
        x = self.parent().pos().x() + self.parent().width() - menu.width()
        y = self.parent().pos().y() + self.pos().y() - menu.height() + 30
        menu.exec(QPoint(x, y))


class ToolBar(QToolBar):
    def __init__(self, parent: QMainWindow, area: Qt.ToolBarArea = Qt.TopToolBarArea):
        super().__init__()
        self.setMovable(False)
        parent.addToolBar(area, self)


class SideBar(ToolBar):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent, Qt.LeftToolBarArea)


def test():
    import sys

    from AutoLab.utils.qthelpers import qapplication

    app = qapplication()
    win = QMainWindow()
    win.setWindowTitle("Test")
    win.resize(900, 300)
    StatusBar(win)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    test()
