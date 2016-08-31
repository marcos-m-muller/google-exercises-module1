#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def open_file(fn):
    file = open(fn,'r')
    return file


def file_content(fn):
    file = open_file(fn)
    return file.read().replace('\n', ' ').split()


def create_dic(dic, words):
    for i,p in enumerate(words):
        if p not in dic.keys():
            dic[p] = []

        if i < len(words) - 1:
            dic[p].append(words[i + 1])
    return


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    # +++your code here+++
    content = file_content(filename)
    mimic = {'':[content[0]]}
    create_dic(mimic, content)
    return mimic


def print_mimic(dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # +++your code here+++
    chosen_words = []
    line_length = 0
    for i in range(200):
        if dict[word]:
            word = random.choice(dict[word])
        else:
            word = ''

        if line_length <= 70:
            chosen_words.append(word)
            line_length += len(word)
        else:
            print(' '.join(chosen_words), end='\n')
            line_length = 0
            chosen_words.clear()


    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
