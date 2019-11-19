# TreeFinder
![Alt text](img.png?raw=true "IMG")

Simple script useful to search for a string in specific files using wildcards. This script reads files and scans them line by line, and returns the matching lines and their index in a TXT report.
Similar to ``` grep -rnw '/path/to/somewhere/' -e 'pattern' ```
but with a fancier interface.

## Requirements
You will need Python 3.6.X or later, ``` colorama``` (for fancy colors) and ``` pathlib```. Windows 7, 8, 10 - Linux tested
```bash
pip install colorama pathlib
```

## Pyinstaller
If you want to create a standalone executable, run the following commands
```bash
pip install pyinstaller
pyinstaller /path/to/TreeFinder.py --onefile -y
```

## Using TreeFinder
### Start
Launch the script with 
```bash
python /path/to/TreeFinder.py 
```
or double-click if you created a standalone executable 

### Usage
``` Folder to scan : [default : current directory] ``` : 
Type the directory you want to scan (Example : E:\Softwares\Sources) or leave it blank to scan the script's parent directory)

``` Files to scan (use wildcards) : [default : * (all)]``` : 
Type the files you want to scan, using wildcards (Example : ``` *.cpp```, ``` report??.txt```, etc) or leave it blank to scan all files

``` String to find : (use wildcards)``` :
Type the string you want to find, using wildcards (Example : ``` hello```, ``` entry[!abc]```, etc)


The script will now scan the directory, a report is available in the script's parent directory.
