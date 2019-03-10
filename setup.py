# -*- coding: utf-8 -*-

import os.path

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

setup(
    name='galvani',
    version='0.0.1a1',
    description='Open and process battery charger log data files',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/chatcannon/galvani',
    author='Chris Kerr',
    author_email='chris.kerr@mykolab.ch',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
    ],
    packages=['galvani'],
    entry_points={'console_scripts': [
            'res2sqlite = galvani.res2sqlite:main',
    ]},
    install_requires=['numpy'],
)
