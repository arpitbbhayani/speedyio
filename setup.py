from distutils.core import setup
from setuptools import find_packages


setup(
    name = 'speedyio',
    packages = find_packages(),
    version = '0.2',
    description = 'Input from console made easy and interactive for Python',
    author = 'Arpit Bhayani',
    author_email = 'arpit.b.bhayani@gmail.com',
    url = 'https://github.com/arpitbbhayani/speedyio',
    download_url = 'https://github.com/arpitbbhayani/speedyio',
    keywords = ['io', 'cli'],
    classifiers = [],
    install_requires = [
        'inquirer==2.1.11'
    ]
)
