"""
This code calculates a new hashtable and should be run every time datafiles
"""


import os, json, time
import hashlib
from plasmapydata import _root_dir

from plasmapy.utils.data.downloader import filehash






def make_hashtable():
    
    # Create a list of files
    files= list( os.walk((os.path.join(_root_dir, 'data'))) )[0][2]
    
    # Hash every file
    hashdict = {}
    for file in files:
        
        # Remove the currently existing hashtable
        if 'hashtable' in file and '.json' in file:
            os.remove(file)
        else:
            hashdict[file] = filehash(os.path.join(_root_dir, 'data', file))
            
            
    # Use the current time in seconds as a hash for the hashtable itself
    with open(f'hashtable-{int(time.time())}.json', 'w') as f:
        json.dump(hashdict, f)
        

if __name__ == '__main__':
    make_hashtable()