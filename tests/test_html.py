import os
import drivers

def test_html_lib():
    html = "<html><style></style><body><h1><b>Hello,</b></h1><h2><i> world</i></h2></body></html>"
    text = drivers.html.to_text(html)
    assert 'Hello, world' in text

def test_html_bin():
    html = "<html><style></style><body><h1><b>Hello,</b></h1><h2><i> world</i></h2></body></html>"
    pipe = os.popen(f"echo '{html}' | html")
    assert 'Hello, world' in pipe.read()
