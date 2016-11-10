import os
import re
from bs4 import BeautifulSoup


def parse(path=None, output=None, recursive=False):

    if recursive:
        for filename in os.listdir(path):
            parse(path + filename, path + filename + '.txt', False)

    else:
        html = open(path, 'r')
        html = BeautifulSoup(html, 'html.parser')
        text = html.get_text()

        if output is None:
            return text
        else:
            f = open(output, 'w')
            f.write(text.encode('utf8'))
            f.close
            return text
