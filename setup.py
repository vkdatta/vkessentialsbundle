from setuptools import setup

setup(
  name='termuxessentialsbyvk',
  version='0.0',
  description='A lightweight Termux toolkit to copy, erase, overwrite file content and scrape web tables/links with a single command.',
  author='vkd',
    scripts=['script/copy','script/erase','script/overwrite','script/xtract'],
  python_requires='>=3.6',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)
