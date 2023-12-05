import os
from kern import pdf

def test_pdf_lib():
    file = "files/chicken.pdf"
    text = pdf.to_text(file)
    assert 'chicken' in text

    file = "files/chicken.pdf"
    text = pdf.pdf_to_text(file)
    assert 'chicken' in text

def test_pdf_lib_return_pages():
    file = "files/chicken.pdf"
    text = pdf.to_text(file, return_pages=True)
    assert not isinstance(text, str)
    assert all(isinstance(page, str) for page in text)
    assert 'chicken' in '\n\n'.join(text)

    file = "files/chicken.pdf"
    text = pdf.to_text(file, return_pages=False)
    assert isinstance(text, str)
    assert 'chicken' in text

    file = "files/chicken.pdf"
    text = pdf.pdf_to_text(file, return_pages=True)
    assert not isinstance(text, str)
    assert all(isinstance(page, str) for page in text)
    assert 'chicken' in '\n\n'.join(text)

    file = "files/chicken.pdf"
    text = pdf.pdf_to_text(file, return_pages=False)
    assert isinstance(text, str)
    assert 'chicken' in text

def test_pdf_bin():
    pipe = os.popen("cat files/chicken.pdf | pdf")
    assert 'chicken' in pipe.read()
