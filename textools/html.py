import os
import re
from bs4 import BeautifulSoup


def parse(path=None, output=None, recursive=False):

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        for index, filename in enumerate(files):
            parse(path + filename, path + filename + '.txt', False)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

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
