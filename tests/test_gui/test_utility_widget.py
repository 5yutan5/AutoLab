from tests.utils import qtapp_test


@qtapp_test
def test_intslider():
    from AutoLab.widgets.utility_widgets import IntSlider

    int_slider = IntSlider()
    int_slider.range = 1, 100
    assert True


@qtapp_test
def test_pathline():
    from AutoLab.widgets.utility_widgets import PathLine

    path_line = PathLine()
    path_line.update_path("Sample")
    assert True
