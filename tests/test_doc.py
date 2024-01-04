import os
from kern.doc import doc_to_text

def test_doc_lib():
    file = "files/basketball.docx"
    text = doc_to_text(file)
    assert 'basketball' in text

    file = "files/baseball.odt"
    text = doc_to_text(file)
    assert 'baseball' in text

def test_doc_bin():
    pipe = os.popen("cat files/basketball.docx | doc")
    assert 'basketball' in pipe.read()

    pipe = os.popen("cat files/baseball.odt | doc")
    assert 'baseball' in pipe.read()
