# Duplicate-File-Finder
Finds duplicate files and provides analytics tools, including exporting to .csv.

## USAGE (Command-line)
### Args:
`py driver.py [-h] [--path PATH] [--verbose y/n]`

`--path` flag is the current working directory by default.

`--verbose` flag is `y` by default. Also accepts `1`/`0`, `true`/`false`, `t`/`f`, etc.

### To specify a directory:
`py driver.py --path "C://Users/me/Desktop/"`

### To run in the current working directory:
`py driver.py`


Automatically outputs results to a .csv file.
