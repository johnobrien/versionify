#!/usr/bin/python

import sys
import os
import getpass
from datetime import datetime
from shutil import copy


def handler(argv):
    versionify(argv)


def versionify(fp):
    print(fp)
    current_path, original_file_name = os.path.split(fp)

    print("Current Path: {0}".format(sys.argv[0]))
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
        input("Press any key to continue...")
        raise


if __name__ == "__main__":
    handler(sys.argv)
