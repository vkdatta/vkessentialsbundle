# vkessentialsbundle

A tiny CLI bundle for Termux that lets you copy, erase, or overwrite files via your clipboard.

## Installation

```bash
pip install vkessentialsbundle
```

Usage

Copy a file’s contents to clipboard

vkessentials copy XYZ.py

Copies everything inside XYZ.py into your Termux clipboard.

Erase a file’s contents

vkessentials erase notes.txt

Prompts you yes/no; on yes, clears out notes.txt.

Overwrite file with clipboard

vkessentials overwrite draft.md

Pastes whatever’s in your clipboard into draft.md, replacing its previous contents.


Requirements

Termux on Android

termux-api package for clipboard commands

Python 3.6+ and pip
