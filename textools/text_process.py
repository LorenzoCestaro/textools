import re


def clean(text):
    # Remove multiple newlines
    text = re.sub(r'\n+', r'\n', text)

    # Remove non latin characters
    text = re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', u'', text)

    # Remove urls
    text = re.sub(r'(?:http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', u'', text)

    return text
