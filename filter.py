#!/usr/bin/env python
"""
Usage:
  PROG [-C <dir>] <input> <output> [--scripts]
  PROG (-h | --help | --version)

Options:
  -C, --chdir    process local scripts tags
  -s, --scripts  process local scripts tags
  -h, --help     Show this screen and exit.
  <input>        input file  [- means stdin]
  <output>       output file [- means stdout]
"""

import re, os, sys, base64, docopt


__version__ = "1.0.1"


doc = __doc__.replace('PROG', sys.argv[0])


args = docopt.docopt(doc, version=__version__)


if args['<dir>']: os.chdir(args['<dir>'])


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
                  'favicon.ico' ,
                 ]


def process_line(line):

    if 'http' in line:
        
        return line

    if contains(line, '<img ', 'src=', '.jpg'):
        
        if 'http' not in line:

            if m := re.search(r'''src="(.*)"''', line):
                itype = 'image/jpeg'
                data = f"data:{itype};base64," + read_file64(m.group(1))
                s, e = m.span(1)
                return ''+line[:s]+data+line[e:]+''

            pass

        pass
    
    if contains(line, 'background-image', 'url', '.jpg'):

        if m := re.search(r"""url\((.*)\)""", line):
            itype = 'image/jpeg'
            data = f"data:{itype};base64," + read_file64(m.group(1))
            s, e = m.span(1)
            return line[:s]+data+line[e:]

        return '<style>' + read_file(css_file) + '</style>\n'

    if contains(line, '<link', 'stylesheet', css_file):
        
        return '<style>' + read_file(css_file) + '</style>\n'

    for fname in favicon_names:

        for itype in ('image/png', 'image/x-icon'):

            if contains(line, '<link', 'icon', itype, fname):
            
                data = f"data:{itype};base64," + read_file64(fname)
                
                return line.replace(fname, data)

            pass
        
        pass

    def do_img(m, s, e):
        return line[:s]+">"+open(m.group(1)).read().strip()+line[e:]
        
    if args['--scripts'] and contains(line, '<script', 'src=', '</script>'):

        if 'http' not in line:
        
            if m := re.search(r"""src="(.*)"[ \t\r\n]*>""", line):
                return do_img(m, *m.span())
        
            if m := re.search(r"""src='(.*)'[ \t\r\n]*>""", line):
                return do_img(m, *m.span())
        
            if m := re.search(r"""src=([^ \t\r\n>]*)[ \t\r\n]*>""", line):
                return do_img(m, *m.span())
            
            pass
        
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

