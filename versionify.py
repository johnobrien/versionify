#!/usr/bin/python

import sys
import os
from datetime import datetime
from shutil import copy 

current_path, original_file_name  = os.path.split(sys.argv[1])

directory = os.path.join(current_path,  "Old Versions")

if not os.path.exists(directory):
    os.makedirs(directory)

fileName, fileExtension = os.path.splitext(original_file_name)

dt = datetime.now()

versioned_file_name =  fileName + " JO-" + dt.strftime("%A, %d. %B %Y %I%M%S%p") + fileExtension

copy(original_file_name, directory)

os.rename(os.path.join(directory, original_file_name), os.path.join(directory, versioned_file_name))