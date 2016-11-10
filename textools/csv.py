import text_process
import os
import pandas
import re
import html


def parse(path, label, output=None, recursive=None, clean=False):
    output = output if output else path + '.html'

    if recursive:
        files = [f for f in os.listdir(path) if not f.startswith('.')]
        files = [f for f in files if f.endswith('.csv')]
        for index, filename in enumerate(files):
            csv_to_html(path + filename, None, False)
            print 'Parsed document ' + str(index + 1) + ' of ' + str(len(files))

    else:
        csv_file = pandas.read_csv(path)
        csv_file = csv_file[label]
        html_file = open(output, 'w')

        for index, row in csv_file.iteritems():
            row = re.sub('^"', '', row)
            row = re.sub('","', ' ', row)
            row = re.sub('""', '"', row)
            html_file.write(row)

        html_file.close()
        html.parse(path=output, output=None, recursive=False, clean=clean)
