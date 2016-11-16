import os
import textract
import text_process


def parse(path=None, output=None, recursive=False, clean=False):
    output = output if output else path + '.txt'

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.pdf')]
        for index, filename in enumerate(files):
            parse(path + filename, None, False, clean)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        text = textract.process(path)
        if clean:
            text = text_process.clean(text)

        f = open(output, 'w')
        f.write(text)
        f.close()
        return text
