import os
import re
import pytest

def test_pdf_lib():
    from drivers import pdf
    file = "root/usr/share/chicken.pdf"
    text = pdf.to_text(file)
    assert 'chicken' in text

    file = "root/usr/share/chicken.pdf"
    text = pdf.pdf_to_text(file)
    assert 'chicken' in text

def test_pdf_bin():
    pipe = os.popen("cat root/usr/share/chicken.pdf | pdf")
    assert re.search('chicken', pipe.read())
