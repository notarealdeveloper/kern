#!/usr/bin/env python3

__all__ = ['main']

import sys

def main(argv=None):

    import argparse
    from . import is_url
    from . import url_to_html
    from . import html_to_text

    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('html')
    parser.add_argument('path', nargs='?')
    args = parser.parse_args(argv)

    if args.path is not None:
        bytes = open(args.path, 'rb').read()
    else:
        bytes = sys.stdin.buffer.read().decode()

    arg = arg.decode()

    if is_url(arg):
        html = url_to_html(arg)
    else:
        html = arg

    text = html_to_text(html)
    print(text)

if __name__ == '__main__':
    main()
