#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++


    #######################

    # antes de abrir o filename, o conteudo dele é ['animal_code.google.com']
    # vou varer o conteudo para buscar a servidor, que é o que fica após _
    dominio = re.search(r'_(.+)', filename).group(1)
    # domínio = code.google.com

    # criei uma lista que vai receber os resultados
    matches = []

    # abro o filename em f 
    f = open(filename)
  

    for line in f:
        # procurar o conteudo que esta entre o GET e o HTTP, e jogar em match
        match = re.search(r'GET (.+) HTTP', line)

        #se tem "puzzle" no () do match, jogar para matches, com a URL completa
        if "puzzle" in match.group(1):
            matches.append("http://" + dominio + match.group(1))
  
    f.close()

    # vai devolver a lista de URLs em ordem e sem repetição (set ??)
    return sorted(set(matches))


    ########################


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # crio o diretorio
    if not os.path.exists(dest_dir):
        dir_name = dest_dir
        os.mkdir(dir_name)




def main():

    #sys.argv = ['logpuzzle.py', 'animal_code.google.com']
    args = sys.argv[1:]
    # args = ['animal_code.google.com']


    # roda, caso eu nao indique o arquivo, e encerra o programa
    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)




    # coloco na variavel img_urls o conteudo que retorna da funcao read_urls
    # no caso, vai retornar um lista com as urls
    img_urls = read_urls(args[0])
    print('\n'.join(img_urls))

    todir = './imagens'

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
