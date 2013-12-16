from setuptools import setup
from decentscraper import __version__

setup(
    name='decentscraper',
    version=__version__,
    author='John Martin, Sam Wainwright, John Wainwright',
    author_email='john@lonepixel.com',
    packages=['decentscraper'],
    url='https://github.com/thatjohnmartin/decentscraper',
    license='MIT',
    install_requires=['simplejson==2.6.1', 'beautifulsoup4==4.2.1', 'lxml==3.2.1'],
    long_description=open('README.md').read(),
)