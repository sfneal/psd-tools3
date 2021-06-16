#!/usr/bin/env python
import logging
import os

from setuptools import setup, find_packages

logger = logging.getLogger(__name__)


def get_version():
    filename = os.path.join(os.path.dirname(__file__), 'psd_tools', '_version.py')
    with open(filename, 'rb') as fp:
        return fp.read().decode('utf8').split('=')[1].strip(" \n'")


setup(
    name='psd-tools3',
    version=get_version(),
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    url='https://github.com/sfneal/psd-tools3',
    description='Fork of psd-tools for working with Photoshop PSD files',
    long_description=(open('README.rst').read() + "\n\n" + open('CHANGES.rst').read()),
    license='MIT License',
    install_requires=[
        'docopt >= 0.5',
        'packbits',
        'attrs',
        'Pillow',
        'enum34;python_version<"3.4"',
    ],
    keywords="photoshop psd pil pillow",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={'console_scripts': ['psd-tools=psd_tools.__main__:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
