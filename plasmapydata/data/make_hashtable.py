"""
This code calculates a new hashtable and should be run every time datafiles
"""


import os, json, time
import hashlib
from data import root_dir


# Read+hash in chunks in case files are large
# https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
BUF_SIZE = 100
# Create a list of files
files= list( os.walk(root_dir) )[0][2]


# Hash every file
hashdict = {}
for file in files:
    
    # Remove the currently existing hashtable
    if 'hashtable' in file and '.json' in file:
        os.remove(file)
    else:
        sha1 = hashlib.sha1()
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
                
        hashdict[file] =sha1.hexdigest()
        
# Use the current time in seconds as a hash for the hashtable itself
with open(f'hashtable-{int(time.time())}.json', 'w') as f:
    json.dump(hashdict, f)
        
