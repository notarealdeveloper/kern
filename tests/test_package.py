import os
import re
import pytest

def test_drivers_image_to_text():
    pipe = os.popen("cat share/cats.jpg | image")
    assert re.search('cat', pipe.read())

def test_drivers_image_and_text_to_text():
    pipe = os.popen("cat share/cats.jpg | image 'How many cats?'")
    assert re.search('2', pipe.read())

def test_drivers_pdf_to_text():
    pipe = os.popen("cat share/chicken.pdf | pdf")
    assert re.search('chicken', pipe.read())
