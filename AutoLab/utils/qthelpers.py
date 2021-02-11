import functools
from typing import Type

from AutoLab.style.stylesheet import style_sheet
from AutoLab.widgets.dialog import CriticalErrorMessageBox
from AutoLab.widgets.timer import AutolabCountTimer
from AutoLab.widgets.wrapper_widgets import (AutolabAction, PushButton,
                                             ToolButton)
from PyQt5.QtCore import QEventLoop, QObject, QSize, Qt, QTimer
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QWidget


def qapplication():
    autolabApplication = QApplication
    app = autolabApplication.instance()
    if app is None:
        app = autolabApplication(["AutoLab"])
        app.setApplicationName("AutoLab")
        app.setStyleSheet(style_sheet)
    return app


def create_action(
    parent: QObject,
    text: str = None,
    icon: QIcon = None,
    toggled=None,
    triggered=None,
    name: str = None,
    shortcut: str = None,
    enable: bool = True,
) -> AutolabAction:
    action = AutolabAction(parent)
    if text is not None:
        action.setText(text)
    if triggered is not None:
        action.triggered.connect(triggered)
    if toggled is not None:
        action.toggled.connect(toggled)
        action.setCheckable(True)
    if icon is not None:
        action.setIcon(icon)
    if name is not None:
        action.setObjectName(name)
    if shortcut is not None:
        action.setShortcut(QKeySequence(shortcut))
    action.setEnabled(enable)
    return action


def create_push_button(
    clicked=None,
    fixed_width: int = None,
    fixed_height: int = None,
    icon: QIcon = None,
    text: str = None,
    toggled=None,
):
    button = PushButton()
    if clicked is not None:
        button.clicked.connect(clicked)
    if fixed_width is not None:
        button.setFixedWidth(fixed_width)
    if fixed_height is not None:
        button.setFixedHeight(fixed_height)
    if icon is not None:
        button.setIcon(icon)
    if text is not None:
        button.setText(text)
    if toggled is not None:
        button.toggled.connect(toggled)
        button.setCheckable(True)
    return button


def create_timer(parent, timeout=None, enable_counter: bool = False):
    timer = AutolabCountTimer(parent)
    if timeout is not None:
        timer.timeout.connect(timeout)
    timer.enable_counter = enable_counter
    return timer


def create_tool_button(
    arrow_type: Qt.ArrowType = None,
    fixed_height: int = None,
    fixed_width: int = None,
    icon: QIcon = None,
    icon_size: QSize = None,
    is_text_beside_icon: bool = False,
    text: str = None,
    toggled=None,
    triggered=None,
):
    button = ToolButton()
    if arrow_type is not None:
        button.setArrowType(arrow_type)
    if fixed_height is not None:
        button.setFixedHeight(fixed_height)
    if fixed_width is not None:
        button.setFixedWidth(fixed_width)
    if icon is not None:
        button.setIcon(icon)
    if icon_size is not None:
        button.setIconSize(icon_size)
    if is_text_beside_icon:
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    if text is not None:
        button.setText(text)
    if toggled is not None:
        button.toggled.connect(toggled)
        button.setCheckable(True)
    if triggered is not None:
        button.triggered.connect(triggered)
    return button


def add_qLabel(widget: QWidget, text: str) -> QWidget:
    h_layout = QHBoxLayout()
    h_layout.addWidget(widget)
    h_layout.addWidget(QLabel(text))
    widget_with_label = QWidget()
    widget_with_label.setLayout(h_layout)
    return widget_with_label


def reconnect_slot(signal, new_slot, old_slot=None) -> None:
    if old_slot is not None:
        signal.disconnect(old_slot)
    else:
        signal.disconnect()
    signal.connect(new_slot)


def sleep_nonblock_window(millisecond: int) -> None:
    loop = QEventLoop()
    QTimer.singleShot(millisecond, loop.quit)
    loop.exec()


def popup_exception_message(
    message_box: Type[CriticalErrorMessageBox],
    exception: Type[Exception],
    parent: QWidget = None,
):
    def _popup_exception_message(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception as e:
                message_box(text=str(e), parent=parent).exec()

        return wrapper

    return _popup_exception_message
