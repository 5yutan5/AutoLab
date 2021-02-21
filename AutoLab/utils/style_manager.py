from pathlib import Path
from typing import Union

import AutoLab.icons.dark_theme_icons_rc
import AutoLab.icons.resource_icons_rc
from PySide6.QtWidgets import QApplication, QWidget


def add_style_sheet(widget: Union[QWidget, QApplication], style_sheet: str) -> None:
    marge_style_sheet = widget.styleSheet() + style_sheet
    widget.setStyleSheet(marge_style_sheet)


def change_style_sheet(widget: Union[QWidget, QApplication], style_sheet: str) -> None:
    widget.setStyleSheet(style_sheet)


def load_style_sheet(sheet_name: str) -> str:
    sheet_dir_path = Path(__file__).parent.parent / "style"
    sheet_path = sheet_dir_path / f"{sheet_name}.qss"
    with open(str(sheet_path), "r") as f:
        return f.read()
