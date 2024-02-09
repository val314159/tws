#!/usr/bin/env python
"""
Usage:
  PROG <input> <output>
  PROG (-h | --help | --version)

Options:
  -h, --help  Show this screen and exit.
  <input>     input file  [- means stdin]
  <output>    output file [- means stdout]
"""

import os, sys, base64, docopt

__version__ = "1.0.1"

doc = __doc__.replace('PROG', sys.argv[0])

args = docopt.docopt(doc, version=__version__)

def contains(line, *stuff):
    for thing in stuff:
        if thing not in line:
            return False
        pass
    return True


def read_file(fname):
    return open(fname).read()


def read_file64(fname):
    return base64.b64encode(
        open(fname, 'rb').read()).decode()


css_file = 'site.css'


favicon_names = [ 'favicon-16x16.png' ,
                  'favicon-32x32.png' ,
                 ]


def process_line(line):

    if contains(line, '<link', 'stylesheet', css_file):
        
        return '<style>' + read_file(css_file) + '</style>\n'

    for fname in favicon_names:
        
        if contains(line, '<link', 'icon', fname):
            
            data = "data:image/x-icon;," + read_file64(fname)
            
            return line.replace(fname, data)

        pass
    
    return line


def get_input():
    
    x = args['<input>']
    
    if x == '-':
        return sys.stdin
    
    return open(x)


def get_output():
    
    x = args['<output>']
    
    if x == '-':
        return sys.stdout
    
    return open(x,'w')


output = get_output()

for line in get_input():
    
    print(process_line(line), end='', file=output)

