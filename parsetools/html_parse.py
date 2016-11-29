from bs4 import BeautifulSoup
import os
import re
from settings import BS4_PARSER
import sys
import utils


def parse(path=None, output=None, recursive=False, clean=False):
    """
    Parse html source text from single or multiple files and write results to .txt.
    @params:
        path      - Required : file or directory to parse (Str)
        output    - Optional : output filename (use only if parsing single files) (Str)
        recursive - Optional : recursive execution for directories (Bool)
        clean     - Optional : preprocessing of the input with utils.clean (Bool)
    @returns:
        text      - The processed text
    """
    output = output if output else path + '.txt'

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.html')]
        for index, filename in enumerate(files):
            parse(path + filename, None, False, clean)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        utils.progressbar_update(0, path)
        read_size = 0
        f = open(output, 'w+')
        for index, line in enumerate(open(path)):
            read_size += sys.getsizeof(line)

            line = BeautifulSoup(line, BS4_PARSER)
            for script in line(['script', 'style']):
                script.extract()

            text = line.get_text()
            text = utils.clean(text) if clean else text
            f.write(text.encode('utf8'))

            utils.progressbar_update(read_size, path)

        f.close()
        return text
