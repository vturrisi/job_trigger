import codecs
import os
import sys
from setuptools import setup


VERSION = '0.0.1'

setup(
    name='job_triggerer',
    packages=['job_triggerer'],
    version=VERSION,
    description='Job Triggererer',
    license='MIT',
    author='Victor Turrisi',
    author_email='vt.turrisi@gmail.com',
    url='https://github.com/vturrisi/job_triggerer',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)