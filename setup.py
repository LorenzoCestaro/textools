from setuptools import setup

setup(
    name='textools',
    version='1.0.0',
    description='Tools for extraction of text from pdf and html documents based on textract and beautiful soup',
    author='LorenzoCestaro',
    author_email='lorenzo@igenius.com',
    packages=['textools'],
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'textract',
    ],
    scripts=[
        'bin/parsepdf',
        'bin/parsehtml',
    ],
    zip_safe=False
)
