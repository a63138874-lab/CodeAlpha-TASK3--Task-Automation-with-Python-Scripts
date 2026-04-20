# CodeAlpha-TASK3--Task-Automation-with-Python-Scripts 

This is a simple Python automation project made for moving `.jpg` files from one folder to another using `os` and `shutil`.

## Project Goal
The goal of this task is to automate a small repetitive task using Python.

## Features
- Moves all `.jpg` files from `source_folder` to `destination_folder`
- Uses `os` for folder and file handling
- Uses `shutil.move()` to move files
- Works on Windows

## Folder Structure
project-folder/
├── TAskAutomation.py
├── source_folder/
└── destination_folder/

## What It Does
- Takes all `.jpg` files from `source_folder`
- Moves them to `destination_folder`
- Uses `os` and `shutil`

## Files Used
- `TAskAutomation.py` - main Python script
- `source_folder` - input folder
- `destination_folder` - output folder

## How to Run
1. Put some `.jpg` files inside `source_folder`
2. Open terminal in the project folder
3. Run this command:

```bash
python TAskAutomation.py
```

## Example Output
```bash
moved: daisyflower.jpg
moved: Pink_flower.jpg
moved: yellow petal flower.jpg
done

```
## What I Learned
I learned how to work with folders, files, and moving files using Python.

## Note
This script only moves `.jpg` files.

