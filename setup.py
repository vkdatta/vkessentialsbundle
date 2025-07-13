from setuptools import setup

setup(
  name='vkessentialsbundle',
  version='0.1.0',
  description='Termux clipboard copy/erase/overwrite utilities',
  author='vk',
  scripts=['bin/vkessentials'],
  python_requires='>=3.6',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)
