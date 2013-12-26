from setuptools import setup

setup(
    name='decentscraper',
    version='0.1.0',
    author='John Martin, Sam Wainwright, John Wainwright',
    author_email='john@lonepixel.com',
    packages=['decentscraper'],
    url='https://github.com/thatjohnmartin/decentscraper',
    license='MIT',
    install_requires=['simplejson==2.6.1', 'beautifulsoup4==4.2.1', 'lxml==3.2.1'],
    long_description=open('README.md').read(),
)