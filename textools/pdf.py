import os
import textract


def parse(path=None, output=None, recursive=False):

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.pdf')]
        for index, filename in enumerate(files):
            parse(path + filename, path + filename + '.txt', False)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        text = textract.process(path)
        if output is None:
            return text
        else:
            f = open(output, 'w')
            f.write(text)
            f.close
            return text
