import sys

from AutoLab.utils.icon_manager import IconNames, create_qicon
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication([])
widget = QWidget()
g_layout = QGridLayout(widget)
COLUMN_NUM = 6
for i, icon_name in enumerate(IconNames):
    push_btn = QPushButton(f"  {icon_name.name}")
    push_btn.setIcon(create_qicon(icon_name))
    g_layout.addWidget(push_btn, int(i / COLUMN_NUM), i % COLUMN_NUM)  # type: ignore
widget.show()
sys.exit(app.exec_())
