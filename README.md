## vkessentialsbundle

A small handy bundle for Termux that lets you copy, erase, and overwrite files via commands. 

## Installation

```bash
pip install git+https://github.com/vkdatta/vkessentialsbundle.git
```

## Usage

__Copy a file’s contents to clipboard__

```bash
copy xyz.py
```
Copies everything inside xyz.py into your Termux clipboard.

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

## Pre Requirements

```bash
pkg install -y termux-api python git curl
```
