## vkessentialsbundle

A small handy bundle for Termux that lets you ```copy```, ```erase```, and ```overwrite``` contents inside a file via these simple commands. 

Plus ```xtract``` web scraper tool that extracts link/tables from multiple web pages!

## Installation

```bash
pip install git+https://github.com/vkdatta/termuxessentialsbyvk.git
```

## Upgrade

If the ```copy```, ```erase```, ```overwrite```, ```xtract``` commands are not working as intended, there might be a possible update in this code. 

As this is a tiny personal project, no upgrades are directly provided, and all changes are made to the main version itself. So force install the code for better performance. 

```bash
pip install --upgrade --force-reinstall git+https://github.com/vkdatta/termuxessentialsbyvk.git
```

## Usage

| Command | Example | Usage |
| --- | --- | --- |
| ```copy <filename>``` | ```copy xyz.py``` | Copies everything inside xyz.py into your clipboard. |
| ```erase <filename>``` | ```erase notes.txt``` | erases content of notes.txt. |
| ```overwrite <filename>``` | ```overwrite draft.md``` | overwrites/replaces draft.md content With text in your clipboard |
| ```xtract``` | ```xtract``` | Lets you extract links/tables from websites |

____

Here,  
Enter: ```xyz.com/list/``` to extract tables/links from that page only  
Enter: ```xyz.com/list/100``` to extract tables/links from 100th page only  
Enter: ```xyz.com/list/{100}``` to extract tables/links from 1st page to 100th page  

In addition, You can use multiple URLs from multiple sites using space/comma separation!! Also you can extract only tables/links from specific IDs or Classes

Like 🤔?

```bash
xyz.com/list/{133}, pqr.com/p.html, 123apps.com/alltoolslist/2
```

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
```bash
pip install openpyxl 
```
