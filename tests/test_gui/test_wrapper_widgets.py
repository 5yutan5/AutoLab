from PySide6.QtWidgets import QMainWindow, QToolButton, QWidget
from tests.utils import qtapp_test


@qtapp_test
def test_aaction():
    from AutoLab.widgets.wrapper_widgets import AAction

    action = AAction()
    action.setText("Action ToolButton")
    action_tool_button = QToolButton()
    action_tool_button.setDefaultAction(action)
    action_tool_button.show()
    assert True


@qtapp_test
def test_ahboxLayout():
    from AutoLab.widgets.wrapper_widgets import AHBoxLayout

    widget = QWidget()
    h_layout = AHBoxLayout()
    widget.setLayout(h_layout)
    widget.show()
    assert True


@qtapp_test
def test_alabel():
    from AutoLab.widgets.wrapper_widgets import ALabel

    label = ALabel()
    label.show()
    label = ALabel("Test")
    label.show()


@qtapp_test
def test_apushbutton():
    from AutoLab.widgets.wrapper_widgets import APushButton

    push_button = APushButton("PushButton")
    push_button.show()
    assert True


@qtapp_test
def test_atoolbutton():
    from AutoLab.widgets.wrapper_widgets import AToolButton

    tool_button = AToolButton()
    tool_button.setText("ToolButton")
    tool_button.show()
    assert True


@qtapp_test
def test_atoolbar():
    from AutoLab.widgets.wrapper_widgets import AToolBar

    win = QMainWindow()
    AToolBar(win)
    win.show()
    assert True


@qtapp_test
def test_AVBoxLayout():
    from AutoLab.widgets.wrapper_widgets import AVBoxLayout

    widget = QWidget()
    h_layout = AVBoxLayout()
    widget.setLayout(h_layout)
    widget.show()
    assert True
