from setuptools import setup

setup(
    name='textools',
    version='1.0.0',
    description='Tools for text extraction from pdf and html documents based on textract and beautiful soup',
    author='LorenzoCestaro',
    author_email='lorenzo@igenius.com',
    packages=['textools'],
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'pandas'
        'textract',
    ],
    scripts=[
        'bin/htmlparse',
        'bin/pdfparse',
        'bin/csvparse',
    ],
    zip_safe=False
)
