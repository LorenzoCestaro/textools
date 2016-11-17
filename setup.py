from setuptools import setup

setup(
    name='parsetools',
    version='0.2.1',
    description='Tools for text extraction from pdf and html documents based on textract and beautiful soup',
    author='Lorenzo Cestaro',
    author_email='lorenzo@igenius.net',
    license='MIT',
    url='https://github.com/LorenzoCestaro/parsetools',
    download_url='https://github.com/LorenzoCestaro/parsetools/tarball/0.1.3',
    packages=['parsetools'],
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'pandas',
        'textract',
    ],
    scripts=[
        'bin/htmlparse',
        'bin/pdfparse',
        'bin/csvparse',
    ],
    zip_safe=False
)
