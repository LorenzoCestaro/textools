import re


def clean(text):
    text = text.lower()
    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)

    # Remove urls
    text = re.sub(r'(?:http[s]?://)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    return text
