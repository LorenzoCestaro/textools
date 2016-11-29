# -*- coding: utf-8 -*-

import csv
import re
import settings as s
import sys

# Increase csv library limit for csv line dimensions
csv.field_size_limit(sys.maxsize)


def clean(text):
    """
    Computes simple preprocessing on the input text
    @params:
        text - Required  : text to process (Str)
    """
    text = text.lower() if s.TO_LOWERCASE else text
    text = text.upper() if s.TO_UPPERCASE else text

    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text) if s.REMOVE_MULTIPLE_NEWLINES else text

    # Remove urls
    regex = r'(?:http[s]?://)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    text = re.sub(regex, '', text) if s.REMOVE_URLS else text

    # Remove non ascii characters
    regex = re.compile(ur'[^\x00-\x7F]+', re.UNICODE)
    text = re.sub(regex, '', text) if s.ONLY_ASCII else text

    # Remove lines with less than n words
    if s.REMOVE_SHORT_LINES:
        lines = iter(text.splitlines())
        text = ''
        for line in lines:
            if len(line.split(' ')) >= s.MINIMUM_WORDS:
                text += line + '\n'

    return text


def readcsv(path):
    """
    Read csv line by line and return a dictionary of label:value pairs
    @params:
        path - Required : path to the input csv file (Str)
    """
    for index, line in enumerate(csv.reader(open(path, 'r'))):
        if index == 0:
            labels = line
            continue

        result = dict()
        for i, label in enumerate(labels):
            try:
                result[label] = line[i]
            except:
                result[label] = ''

        result['size'] = sys.getsizeof(','.join(line))

        yield result


def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def progressbar_update(done, path):
    """
    Update state of terminal progress bar for tracking file reading. It compares
    the size of the target file with the size of the data processed until
    invocation.
    @params:
        done - Required : bytes of file read until invocation (Int)
        path - Required : path to the file that is being read (Int)
    @returns:
        printProgress() : function that renders the progress bar
    """
    tot = os.path.getsize(path)
    filename = path.split('/')[-1]

    return printProgress(
        done,
        tot,
        prefix='Reading %s:' % filename,
        suffix='Complete',
        barLength=50
    )
