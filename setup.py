from setuptools import setup
from codecs import open
from os import path


try:
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as file_:
        long_description = file_.read()
except FileNotFoundError:
    # Only occurs when testing
    long_description = ''


setup(
    name='typy',
    version='0.1',
    description='A static type checker for Python 3',
    long_description=long_description,
    url='https://github.com/Procrat/typy',
    author='Stijn Seghers',
    author_email='stijnseghers@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    keywords='type checking testing development',
    packages=['typy'],
    entry_points={
        'console_scripts': [
            'typy=typy:main',
        ],
    },
    tests_require=['pytest'],
)
