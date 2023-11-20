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

def test_drivers_html_to_text():
    html = "<html><style></style><body><h1><b>Hello,</b></h1><h2><i> world</i></h2></body></html>"
    pipe = os.popen(f"echo '{html}' | html")
    assert re.search('Hello, world', pipe.read())
