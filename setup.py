# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from crawltools import __version__


setup(
    name                = 'crawltools',
    version             = __version__,
    description         = 'Simple crawlers',
    long_description    = open('README.md').read(),
    author              = 'Jiun Bae',
    author_email        = 'maytryark@gmail.com',
    url                 = 'https://github.com/jiunbae/crawler',
    download_url        = 'https://github.com/jiunbae/crawler/releases/latest',
    license             = 'MIT',
    keywords            = ['crawler', 'scrapy'],
    python_requires     = '>= 3',
    install_requires    = (
        "scrapy==2.11.1",
        "tqdm",
        "pillow",
    ),
    scripts             = ['bin/crawler', ],
    packages            = find_packages(exclude=['docs', 'tests*']),
    classifiers         = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
