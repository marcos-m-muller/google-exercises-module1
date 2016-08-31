#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def open_file(fn):
    file = open(fn,'r')
    return file


def file_content(fn):
    file = open_file(fn)
    return file.read()


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    log_content = file_content(filename)
    base_url = 'http://' + filename.split('_')[1]
    puzzle_urls_found = re.findall(r'GET (.*puzzle.*?\.jpg|png|bmp|gif) ', log_content)
    url_map = []
    for url in puzzle_urls_found:
        image_name = re.search(r'^/(.+/)*(.+)\.(.+)$', url).group(2).split('-')
        image_name = image_name[-1] if len(image_name) > 1 else '-'.join(image_name)
        url_map.append((image_name,base_url + url))

    #removing duplicates
    dic = dict(url_map)
    #sorting by file name
    url_map = sorted(dic.items(), key=lambda x: x[0])

    return_list = []
    for url in url_map:
        return_list.append(url[1])

    return return_list

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """

    html = open('index.html','w')
    html.write('<html>\n<head>\n<title>puzzle</title>\n</head>\n<body>')
    image_name = 0
    for url in img_urls:
        print('Iniciando o download da imagem {}'.format(url))
        nome = create_file_name(dest_dir, image_name, url)
        urllib.request.urlretrieve(url, nome)
        print('Download finalizado')
        image_name += 1
        html.write('<img src="'+nome+'">')

    html.write('</body>\n</html>')

def create_file_name(dest_dir, image_name, url):
    return dest_dir + '\\img' + str(image_name) + '.' + extract_extension(url)


def extract_extension(url):
    extension = re.search(r'^.*\.(.+)$', url).group(1)
    return extension


def main():
    args = sys.argv[1:]
    urls = read_urls('animal_code.google.com')
    #download_images(urls, '.')
    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
