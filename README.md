## termuxessentialsbyvk

A small toolkit for Termux that lets you:  

- **`copy <filename>`**  

  Copy a file’s contents to your system clipboard.

- **`erase <filename>`**  

  Completely wipe out a file’s contents, leaving an empty file behind.

- **`delete <path> or <filename>`**  

  Remove a single file or directory (recursively) with a single command.

- **`overwrite <filename>`**  

  Replace a file’s entire contents with whatever is currently in your clipboard.

- **`create <path> or <filename>`**  

  Create a single file **or** directory in one go.  

- **`open`** (alias: **`o`**)  

  The “omni-tool” launcher — drill into any file or folder and pick from view, edit, share, move, rename, delete, etc., all without leaving your prompt.

- **`xtract`**  

  Scrape **all** HTML tables and hyperlinks from one or more paginated web pages in a single invocation. Perfect for harvesting catalogues, reports, or any tabular data spread across multiple pages.
  
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
| ```list``` | ```list``` | Gives List of all files in your termux directory |

____

For ```xtract```,  
Enter: ```xyz.com/article/``` to extract tables/links from that page only  
Enter: ```xyz.com/article/100``` to extract tables/links from 100th page only  
Enter: ```xyz.com/article/{100}``` to extract tables/links from 1st page to 100th page  

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
