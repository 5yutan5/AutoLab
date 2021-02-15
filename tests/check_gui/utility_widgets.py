import sys

from AutoLab.utils.qthelpers import create_qt_app
from AutoLab.widgets.utility_widgets import IntSlider, PathLine


def path_line():
    app = create_qt_app("Test")
    file_line = PathLine()
    file_line.update_path("C:/test/sample")
    file_line.show()
    sys.exit(app.exec_())


def int_slider():
    app = create_qt_app("Test")
    int_slider = IntSlider()
    int_slider.range = 1, 10
    int_slider.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # path_line()
    int_slider()
