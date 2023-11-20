import os
from drivers import image

def test_image_lib_1_image_to_text():
    path = 'root/usr/share/cats.jpg'
    text = image.to_text(path)
    assert 'cat' in text

def test_image_lib_1_image_and_text_to_text():
    path = 'root/usr/share/cats.jpg'
    text = image.and_text_to_text(path, "How many cats?")
    assert 'cat' in text

def test_image_bin_1_image_to_text():
    pipe = os.popen("cat root/usr/share/cats.jpg | image")
    assert 'cat' in pipe.read()

def test_image_bin_2_image_and_text_to_text():
    pipe = os.popen("cat root/usr/share/cats.jpg | image 'How many cats?'")
    assert '2' in pipe.read()
