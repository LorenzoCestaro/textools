import text_process
import os
import re
from bs4 import BeautifulSoup


def parse(path=None, output=None, recursive=False, clean=False):
    output = output if output else path + '.txt'

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.html')]
        for index, filename in enumerate(files):
            parse(path + filename, None, False, clean)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        html = open(path, 'r')
        html = BeautifulSoup(html, 'html.parser')
        text = html.get_text()
        text = text_process.clean(text) if clean else text
        f = open(output, 'w')
        f.write(text.encode('utf8'))
        f.close()
        return text
