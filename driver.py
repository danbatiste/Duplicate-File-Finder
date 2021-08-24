import filemanager as fm
import os

# Create test file
"""
with open('testfile.big', 'w') as ofile:
    for _ in range(100_000_000):
        ofile.write('0')
print('file written')
"""

hash_logs = {}

def main(path=os.getcwd()):
    global hash_logs
    print(f"the path is {path}")
    context = [os.path.join(path, local_file_path) for local_file_path in os.listdir(path)]
    files = [file_path for file_path in context if os.path.isfile(file_path)]
    directories = [file_path for file_path in context if os.path.isdir(file_path)]
    
    #error_paths = [file_path for file_path in context if (not os.path.isdir(file_path)) and (not os.path.isfile(file_path))]
    #print(f"Error paths: {error_paths}")

    
    file_hashes = [(fm.get_hash(file_path), file_path) for file_path in files]
    for file_hash, file_path in file_hashes:
        if hash_logs.get(file_hash) is None:
            hash_logs.update({ file_hash : [file_path]})
        else:
            hash_logs[file_hash].append(file_path)

    for directory in directories:
        print(f"This is a directory: {directory}")
        main(path=os.path.join(path, directory))

if __name__ == "__main__":
    hash_logs = {}
    main()
    hash_info = fm.hash_info(hash_logs)

    hash_info.export_csv("Test.csv")
