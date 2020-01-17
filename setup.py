# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='crawltools',
    version='0.1.1',
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
