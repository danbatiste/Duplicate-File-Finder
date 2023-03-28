# Duplicate-File-Finder

This GitHub repository provides a tool to scan a directory for duplicate files and provides analytics tools. It consists of two files, `driver.py` and `filemanager.py`.

## Filemanager.py

The `filemanager.py` file provides a set of functions that are used to manage files and folders. It provides functions to get a list of files and directories in a given path, check if a file or directory exists and delete a file or directory. It also provides a function to get the hash of a file, which is used by the `driver.py` file to identify duplicate files.

## Analytics.py

The `analytics.py` file provides analytics tools for analyzing the data stored in the `Hash_info` class. The `get_duplicates` function finds duplicate files based on the hashes stored in `Hash_info`. The `get_stats` function provides statistics on the number of files, their sizes, and the number of duplicates.

## Usage

To use the Duplicate-File-Finder repository, you can run the `driver.py` file with the following command:

```
python driver.py <directory_to_scan> [--verbose]
```

The `<directory_to_scan>` argument specifies the directory to scan for duplicate files. The `--verbose` argument is optional and can be used to output what the scanner is doing to the console.

For example, if you wanted to scan the folder `C:\Users\John\Documents` for duplicate files and output what the scanner is doing to the console, you would run the following command:

```
python driver.py C:\Users\John\Documents --verbose
```

The `driver.py` file will then scan the directory and its subdirectories recursively and count the number of files and directories that it finds. It will store the hashes and corresponding file paths in a log and create a `Hash_info` object using the data. Finally, it will export the data collected to a CSV file with a unique ID.

To use the Duplicate-File-Finder repository programmatically, import the `filemanager.py` and `analytics.py` files into your project. Create an instance of the `Hash_info` class and use the `get_hash`, `safe_listdir`, and `get_dir_info` functions to populate the dictionary with hashes and file paths. Then, use the `get_duplicates` and `get_stats` functions to find duplicate files and get statistics. Finally, use the `export_csv` function to export the data to a CSV file.

Example:

```python
from filemanager import Hash_info, get_hash, safe_listdir, get_dir_info
from analytics import get_duplicates, get_stats

# Create an instance of the Hash_info class
hash_info = Hash_info()

# Populate the dictionary with hashes and file paths
files = safe_listdir('/path/to/directory')
for f in files:
    hash_info.update(get_hash(f), get_dir_info(f))

# Find duplicate files
duplicates = get_duplicates(hash_info.hashes)

# Get statistics
stats = get_stats(hash_info.hashes)

# Export the data to a CSV file
hash_info.export_csv('/path/to/csv/file.csv')
```