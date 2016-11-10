import os
import textract


def parse(path=None, output=None, recursive=False):

    if recursive:
        for filename in os.listdir(path):
            parse(path + filename, path + filename + '.txt', False)

    else:
        text = textract.process(path)
        if output is None:
            return text
        else:
            f = open(output, 'w')
            f.write(text)
            f.close
            return text
