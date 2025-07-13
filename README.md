# vkessentialsbundle

A tiny CLI bundle for Termux that lets you copy, erase, or overwrite files via your clipboard.

## Installation

```bash
pip install git+https://github.com/vkdatta/vkessentialsbundle.git
```

## Usage

__Copy a file’s contents to clipboard__

```bash
copy XYZ.py
```
Copies everything inside XYZ.py into your Termux clipboard.

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

## Requirements

1. termux-api package for clipboard commands
2. Python 3.6+ and pip
