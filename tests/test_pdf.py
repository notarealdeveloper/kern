import os
from kern.pdf import pdf_to_text, pdf_to_pages

def test_pdf_lib():
    file = "files/chicken.pdf"

    text = pdf_to_text(file)
    assert 'chicken' in text

    pages = pdf_to_pages(file)
    assert isinstance(pages, list)
    assert all('chicken' in page for page in pages)

def test_pdf_bin():
    pipe = os.popen("cat files/chicken.pdf | pdf")
    assert 'chicken' in pipe.read()
