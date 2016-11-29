import os
import textract
import utils


def parse(path=None, output=None, recursive=False, clean=False):
    """
    Parse pdf to extract text from single or multiple files and write results to .txt.
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
        files = [f for f in files if f.endswith('.pdf')]
        for index, filename in enumerate(files):
            parse(path + filename, None, False, clean)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        text = textract.process(path)
        if clean:
            text = utils.clean(text)

        f = open(output, 'w')
        f.write(text)
        f.close()
        return text
