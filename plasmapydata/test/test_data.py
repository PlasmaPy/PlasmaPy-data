# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:46:42 2022

@author: pheu
"""

import os, json

from plasmapydata import _root_dir
from  plasmapy.utils.data.downloader import filehash


def test_hashtable():
    """
    Verifies that the hash table is up to date
    """
    data_dir = os.path.join(_root_dir, 'data')
    
    files= list( os.walk(os.path.join(data_dir)) )[0][2]
    
    # Identify and load the hashtable 
    hfile = os.path.join(data_dir,
                            [f for f in files if 'hashtable' in f][0])
    
    with open(hfile, 'r') as f:
        hashdict = json.load(f)
        
    # Remove the hashfile from the list, since it is not in the hashtable
    files = [f for f in files if 'hashtable' not in f]
        

    missing_files = []
    needs_update = []
    for file in files:
        if file not in hashdict.keys():
            missing_files.append(file)
        else:
            h = filehash(os.path.join(data_dir, file))
            if h != hashdict[file]:
                needs_update.append(file)
                
    if len(missing_files + needs_update) > 0:
        raise ValueError("Hashfile is invalid.\n"
                         f"Missing files: {missing_files}\n"
                         f"Out of date files: {needs_update}")
  

if __name__ == '__main__':
    test_hashtable()