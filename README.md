## vkessentialsbundle

A small handy bundle for Termux that lets you ```copy```, ```erase```, and ```overwrite``` contents inside a file via these simple commands. 

Plus ```xtract``` tool that extracts tables from multiple web pages!

## Installation

```bash
pip install git+https://github.com/vkdatta/vkessentialsbundle.git
```

## Upgrade

If the ```copy```, ```erase```, ```overwrite```, ```xtract``` commands are not working as intended, there might be a possible update in this code. 

As this is a tiny personal setup, no upgrades are directly provided, and all changes are made to the main version itself. So force install the code for better performance. 

```bash
pip install --upgrade --force-reinstall git+https://github.com/vkdatta/vkessentialsbundle.git
```

## Usage

__Copy a file’s contents to clipboard__

```bash
copy xyz.py
```
Copies everything inside xyz.py into your clipboard.

__Erase a file’s contents__

```bash
erase notes.txt
```
Prompts you yes/no; on yes, clears out notes.txt.

__Overwrite file with clipboard__

```bash
overwrite draft.md
```
Pastes whatever’s in your clipboard into draft.md, replacing its previous contents.

__xtract__

```bash
xtract
```

And Enter.

This asks URL. 

Enter the URL if you are extracting a single page and enter.
If there are multiple pages attached to a single URL, Like:

xyz.com/list/1
xyz.com/list/2
xyz.com/list/3

Enter: xyz.com/list/{}
And in the number of pages prompt, enter 3

## Pre Requirements

```bash
pkg install termux-api
pkg install python -y
pkg install root-repo
pkg uninstall tur-repo -y
pkg update -y
pkg upgrade -y
pkg install tur-repo -y
pkg install clang libopenblas libffi libzmq build-essential -y
```
```bash
pkg update
pkg install clang make cmake pkg-config
pkg install python-dev
pkg install ninja
pkg install libandroid-spawn
pkg install libffi-dev
```
```bash
pip install numpy
```
```bash
pip install pandas
```
```bash
pkg install -y termux-api python git curl
```
```bash
pip install requests pandas beautifulsoup4 tqdm
```
