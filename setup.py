# -*- coding: utf-8 -*-

from setuptools import setup

from crawler import __version__


setup(
    name='crawltools',
    version=__version__,
    description='Simple crawlers',
    long_description=open('README.md').read(),
    author='jiunbae',
    author_email='maytryark@gmail.com',
    url='https://github.com/maybes/crawler',
    license='MIT',
    install_requires=(
        'scrapy',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
