from image_to_rgb import __version__, main


def test_version():
    assert __version__ == '0.1.0'

def test_get_pixel():
    assert main.getValToWrite(10) == " 10 "

