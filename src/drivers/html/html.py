__all__ = [
    'is_url',
    'url_to_html',
    'html_to_text',
]

def is_url(text):
    import validators
    return bool(validators.url(text))

def url_to_html(url):
    import requests
    return requests.get(url).content.decode()

def html_to_text(text):
    import bs4
    soup = bs4.BeautifulSoup(text, 'html.parser')
    return soup.text

to_text = html_to_text
