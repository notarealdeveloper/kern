import os
from kern import pdf

def test_pdf_lib():
    file = "files/chicken.pdf"
    text = pdf.to_text(file)
    assert 'chicken' in text

    file = "files/chicken.pdf"
    text = pdf.pdf_to_text(file)
    assert 'chicken' in text

def test_pdf_bin():
    pipe = os.popen("cat files/chicken.pdf | pdf")
    assert 'chicken' in pipe.read()
