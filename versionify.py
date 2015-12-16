#!/usr/bin/python

import sys
import os
import getpass
from datetime import datetime
from shutil import copy


def versionify(argv):
    current_path, original_file_name = os.path.split(argv[1])

    print("Current Path: {0}".format(sys.argv[1]))
    try:
        directory = os.path.join(current_path,  "Old Versions")

        if not os.path.exists(directory):
            os.makedirs(directory)

        fileName, fileExtension = os.path.splitext(original_file_name)

        dt = datetime.now()

        versioned_file_name = fileName + "-"\
            + getpass.getuser() + "-"\
            + dt.strftime("%Y.%m.%d.%H.%M.%S") + fileExtension

        copy(original_file_name, directory)

        os.rename(os.path.join(directory, original_file_name),
                  os.path.join(directory, versioned_file_name))

        print("{0} versioned successfully as {1}".format(original_file_name,
                                                         versioned_file_name))
    except Exception:
        raise
    finally:
        input("Press any key to continue...")

if __name__ == "__main__":
    versionify(sys.argv)
