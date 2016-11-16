import re
import settings as s


def clean(text):
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
