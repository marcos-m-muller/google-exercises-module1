#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def open_file(fn):
    file = open(fn,'r')
    return file


def file_content(fn):
    file = open_file(fn)
    return file.read()


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    content = file_content(filename)
    year = extract_year(content)
    return_list = [year]
    names = extract_all_name_rank_lines(content)
    names_rank_list = []
    for matches in names:
        names_rank_list.append("{} {}".format(matches[1], matches[0]))
        names_rank_list.append("{} {}".format(matches[2], matches[0]))

    names_rank_list.sort()
    return_list = return_list + names_rank_list

    return return_list


def extract_all_name_rank_lines(content):
    nomes = re.findall(r'<tr align="right"><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td>', content)
    return nomes


def extract_year(content):
    year = re.search(r'Popularity in (\d{4})', content)
    return year.group(1)


def create_summary_file(filename,list):
    file = open(filename + '.summary', 'w')
    file.write('\n'.join(list) + '\n')


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    for filename in args:
        list = extract_names(filename)
        if not summary:
            print('\n'.join(list) + '\n')
        else:
            create_summary_file(filename,list)


if __name__ == '__main__':
    main()
