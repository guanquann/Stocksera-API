import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.14'
PACKAGE_NAME = 'stocksera'
AUTHOR = 'Guan Quan'
AUTHOR_EMAIL = 'stocksera@gmail.com.com'
URL = 'https://github.com/guanquann/Stocksera-API'

LICENSE = 'The MIT License (MIT)'
DESCRIPTION = 'Official Stocksera API'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ['pandas', 'requests']

CLASSIFIERS = [
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'License :: OSI Approved :: MIT License'
]

PYTHON_REQUIRES = '>=3.6'

KEYWORDS = ["stocks", "wallstreetbets", "trading", "senate", "investing", "finviz"]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      python_requires=PYTHON_REQUIRES,
      keywords=KEYWORDS
      )
