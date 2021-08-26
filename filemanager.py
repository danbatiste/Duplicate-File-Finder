from __future__ import unicode_literals
import hashlib
import os

class Hash_info():
    def __init__(self, hash_logs):
        self.hash_logs = hash_logs
        
    def update_hash_counts(self):
        self.hash_counts = {}
        for k, v in self.hash_logs.items():
            self.hash_counts.update({k:v})

    def export_csv(self, filename):
        with open(filename, 'w') as ofile:
            for k, v in self.hash_logs.items():
                try:
                    ofile.write(f"{k},{len(v)},{v}\n")
                except UnicodeEncodeError:
                    ofile.write(f"{k}, {len(v)}, UnicodeEncodeError")


def safe_listdir(path):
    try:
        return os.listdir(path)
    except PermissionError:
        return []

def get_hash(filename):
    # Hashlib code taken from https://www.pythoncentral.io/hashing-files-with-python/
    hasher = hashlib.md5()
    with open(filename, 'rb') as ifile:
        buf = ifile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def get_dir_info(path):
    files = os.listdir(path)
    is_file_mask = [os.path.isfile(file) for file in files]
    return files, is_file_mask
