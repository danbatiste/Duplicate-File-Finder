import filemanager as fm
import os
import argparse
import time

# Argparse
parser = argparse.ArgumentParser(description="Check for duplicate files.")
parser.add_argument('--path', type=str,
                    help='The folder to (recursively) scan for duplicate files',
                    default=os.getcwd())
parser.add_argument('--verbose', type=str,
                    help='Output what the scanner is doing to the console (True/False, default=True)',
                    default="True")
args = parser.parse_args()
# Bug fix
if args.verbose.lower() in "0 false f n no".split():
    args.verbose = False
elif args.verbose.lower() in "1 true t y yes".split():
    args.verbose = True
else:
    print(f"Unrecognized argument \"{args.verbose}\" for flag --verbose")
    exit()

# Main function
def scan_directory(path=os.getcwd(), verbose=True):
    global hash_logs, file_count, directory_count
    if verbose:
        print(f"Scanning {path}")

    context = [os.path.join(path, local_file_path) for local_file_path in fm.safe_listdir(path)]
    files = [file_path for file_path in context if os.path.isfile(file_path)]
    directories = [file_path for file_path in context if os.path.isdir(file_path)]

    if verbose:
        cwd_file_count = len(files)
        cwd_directory_count = len(directories)
        file_count += cwd_file_count
        directory_count += cwd_directory_count
        print(f"Found {cwd_file_count} files and {cwd_directory_count} directories\n")

    file_hashes = []
    for file_path in files:
        try:
            file_info = (fm.get_hash(file_path), file_path)
            file_hashes.append(file_info)
        except (PermissionError, OSError):
            pass

    for file_hash, file_path in file_hashes:
        if hash_logs.get(file_hash) is None:
            hash_logs.update({ file_hash : [file_path]})
        else:
            hash_logs[file_hash].append(file_path)

    for directory in directories:
        scan_directory(path=os.path.join(path, directory), verbose=verbose)


# Driver code
if __name__ == "__main__":
    if args.verbose:
        print(f"Recursively scanning {args.path}...\n")

    hash_logs, file_count, directory_count = {}, 0, 0 #TODO put all this in the function so globals aren't needed
    scan_directory(args.path, verbose=args.verbose)

    if args.verbose:
        print(f"Scanned {file_count} files and {directory_count} directories")

    hash_info = fm.Hash_info(hash_logs)
    UID = str(int(time.time()))
    hash_info.export_csv(f"output_{UID}.csv")
