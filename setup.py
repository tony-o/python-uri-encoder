from setuptools import setup

setup(
  name='URI',
  version='0.0.0',
  author='Tony O\'Dell',
  author_email='tony.odell+python@live.com',
  packages=['URI.Encoder'],
  url='https://github.com/tony-o/python-uri-encoder',
  license='LICENSE',
  description='A uri component encoder/decoder',
  long_description=open('README.md').read(),
  install_requires=['unittest'],
);
