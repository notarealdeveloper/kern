import os
from drivers import pdf

def test_pdf_lib():
    file = "root/usr/share/chicken.pdf"
    text = pdf.to_text(file)
    assert 'chicken' in text

    file = "root/usr/share/chicken.pdf"
    text = pdf.pdf_to_text(file)
    assert 'chicken' in text

def test_pdf_bin():
    pipe = os.popen("cat root/usr/share/chicken.pdf | pdf")
    assert 'chicken' in pipe.read()
