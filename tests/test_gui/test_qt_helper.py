from time import time

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from tests.utils import qtapp_test


@pytest.mark.skipif(True, reason="Utility function")
def toggle_action(self):
    pass


@pytest.mark.skipif(True, reason="Utility function")
def triggere_action(self):
    pass


@pytest.mark.skipif(True, reason="Utility function")
def click_action(self):
    pass


@qtapp_test
def test_add_unit():
    from AutoLab.utils.qthelpers import add_unit

    widget = QWidget()
    add_unit(widget, "cm")
    return True


@qtapp_test
def test_create_action():
    from AutoLab.utils.qthelpers import create_action

    parent_widget = QWidget()

    text = "Action"
    name = "Test Action"
    shortcut = "A"
    action = create_action(
        parent=parent_widget,
        text=text,
        toggled=toggle_action,
        triggered=triggere_action,
        name=name,
        shortcut=shortcut,
        enable=True,
    )
    assert action.text() == text and action.objectName() == name


@qtapp_test
def test_create_pushbutton():
    from AutoLab.utils.qthelpers import create_push_button

    text = "Test Push Button"
    fixed_width = 150
    fixed_height = 150
    button = create_push_button(
        clicked=click_action,
        fixed_height=fixed_height,
        fixed_width=fixed_width,
        text=text,
        toggled=toggle_action,
    )
    assert (
        button.height() == fixed_height
        and button.width() == fixed_width
        and button.text() == text
    )


@qtapp_test
def test_create_toolButton():
    from AutoLab.utils.qthelpers import create_tool_button

    text = "Test Tool Button"
    fixed_width = 150
    fixed_height = 150
    button = create_tool_button(
        arrow_type=Qt.UpArrow,
        fixed_height=fixed_height,
        fixed_width=fixed_width,
        is_text_beside_icon=True,
        text=text,
        toggled=toggle_action,
        triggered=triggere_action,
    )
    assert (
        button.height() == fixed_height
        and button.width() == fixed_width
        and button.text() == text
    )


@qtapp_test
def test_create_qt_app():
    from AutoLab.utils.qthelpers import create_qt_app

    app_list = []
    for _ in range(2):
        app_list.append(create_qt_app())
    print(app_list)
    assert app_list[0] is app_list[1]


@qtapp_test
def test_sleep_nonblock_window():
    from AutoLab.utils.qthelpers import sleep_nonblock_window

    start = time()
    sleep_nonblock_window(3000)
    assert int(time() - start) == 3
