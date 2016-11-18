import html_parse
import os
import pandas
import re
import utils


def parse(path, label, output=None, recursive=None, clean=False):
    output = output if output else path + '.html'

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.csv')]
        for index, filename in enumerate(files):
            parse(path + filename, label, None, False, clean)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        progressbar_update(0, path)
        read_size = 0
        html_file = open(output, 'w+')
        for index, row in enumerate(utils.readcsv(path)):
            read_size += row['size']
            row = row[label]
            regex = re.compile(ur'[^\x00-\x7F]+', re.UNICODE)
            row = re.sub(regex, '', row)
            row = re.sub('[\n\t\r]', '', row)
            row = re.sub('<article', '\n<article', row)
            html_file.write(row)

            progressbar_update(read_size, path)

        html_file.close()
        html_parse.parse(path=output, output=None, recursive=False, clean=clean)


def progressbar_update(done, path):
    tot = os.path.getsize(path)
    filename = path.split('/')[-1]

    return utils.printProgress(
        done,
        tot,
        prefix='Reading %s:' % filename,
        suffix='Complete',
        barLength=50
    )
