#!usr/bin/env python3

import os
import datetime

def create_files_and_their_time_dict(path = './'):
    files = {}
    for filename in os.listdir(path):
        fullname = path + filename
        files[fullname] = os.path.getmtime(fullname)
    return files

def linux_time_to_utc_time(files):
    for filename, linux_time in files.items():
        files[filename]=datetime.datetime.utcfromtimestamp(linux_time).isoformat()
    return files
        
