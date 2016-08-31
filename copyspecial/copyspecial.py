#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
#


import sys
import re
import os
import shutil
import zipfile
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    return [f for f in os.listdir(dir) if os.path.isfile(f) and re.search(r'.*__\w+__.*',f)]


def copy_to(files, destiny_dir):
    for file in files:
        shutil.copy(file, destiny_dir)


def zip_to(files, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as my_zip_file:
        for file in files:
            my_zip_file.write(file)



def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    files = get_special_paths('.')
    copy_to(files, '..')
    zip_to(files, 'test.zip')
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()
