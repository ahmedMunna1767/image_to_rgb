from image_to_rgb import __version__, image_to_text

def test_version():
    assert __version__ == '0.1.0'

def test_get_pixel():
    assert image_to_text.getValToWrite(1)   == "  1 "
    assert image_to_text.getValToWrite(10)  == " 10 "
    assert image_to_text.getValToWrite(100) == "100 "
    assert image_to_text.getValToWrite(100) != "000 "
    assert image_to_text.getValToWrite(100) == "100 "

