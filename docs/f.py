#!/usr/bin/env python

import re, os, sys

infile = open(sys.argv[1]) if os.isatty(0) else sys.stdin

def extract(ws, t, attrs, body=''):
    if body: body = ' ' + body
    if m2 := re.match('(.*?)class="(.*?)"(.*)$', attrs):
        cl = m2.group(2).replace(' ', '.')
        #cl = cl.replace(':','__COLON__')
        #cl = cl.replace('/','__SLASH__')
        #cl = cl.replace('[','__OPEN___')
        #cl = cl.replace(']','__CLOSE__')
        cl = cl.strip()
        if x := (m2.group(1) + m2.group(3)).strip():
            print(f"{ws}{t}.{cl}({x}){body}")
        else:
            print(f"{ws}{t}.{cl}{body}")
    elif attrs:
        print(f"{ws}{t}({attrs}){body}")
    else:
        print(f"{ws}{t}{body}")
        pass
    pass


for line in infile:

    line = line.replace('\t',' '*8)
    
    if   m := re.match(r'(\s*)$', line):
        pass
    
    elif m := re.match(r'(\s*)<!--', line):
        pass
    
    elif m := re.match(r'(\s*)<!', line):
        print("!!!5")

    elif m := re.match(r'(\s*)<html (.*?)>', line):
        print(f"html({m.group(2)})")

    elif m := re.match(r'(\s*)<hr\s*/?>', line):
        print(f"{m.group(1)}hr")

    elif m := re.match(r'(\s*)<(meta|x?link) (.*?)\s*/?>', line):
        print(f"{m.group(1)}{m.group(2)}({m.group(3)})")

    elif m := re.match(r'(\s*)<(x?script) (.*?)></x?script>', line):
        print(f"{m.group(1)}{m.group(2)}({m.group(3)})")

    elif m := re.match(r'(\s*)<title>(.*?)</title>', line):
        print(f"{m.group(1)}title {m.group(2)}")

    elif m := re.match(r'(\s*)<div>$', line):
        print(f"{m.group(1)}div")

    elif m := re.match(r'(\s*)<style>$', line):
        print(f"{m.group(1)}style")

    elif m := re.match(r'(\s*)<nav>$', line):
        print(f"{m.group(1)}nav")

    elif m := re.match(r'(\s*)<footer (.*?)>$', line):
        extract(m.group(1), 'footer', m.group(2))

    elif m := re.match(r'(\s*)<div (.*?)>(.*?)</div>', line):
        extract(m.group(1), 'div', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<div (.*?)>$', line):
        extract(m.group(1), 'div', m.group(2))

    elif m := re.match(r'(\s*)<div (.*?)>(.*?)', line):
        nope
        print(f"{m.group(1)}div({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<svg (.*?)>(.*?)</svg>', line):
        extract(m.group(1), 'svg', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<a (.*?)>(.*?)</a>', line):
        extract(m.group(1), 'a', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<time (.*?)>(.*?)</time>', line):
        extract(m.group(1), 'time', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<span (.*?)>(.*?)</span>', line):
        extract(m.group(1), 'span', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<span (.*?)>$', line):
        extract(m.group(1), 'span', m.group(2))

    elif m := re.match(r'(\s*)<figure>(.*?)</figure>', line):
        extract(m.group(1), 'figure', m.group(2))

    elif m := re.match(r'(\s*)<h1 (.*?)>(.*?)</h1>', line):
        extract(m.group(1), 'h1', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h2 (.*?)>(.*?)</h2>', line):
        extract(m.group(1), 'h2', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h3 (.*?)>(.*?)</h3>', line):
        extract(m.group(1), 'h3', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h4 (.*?)>(.*?)</h4>', line):
        extract(m.group(1), 'h4', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h5 (.*?)>(.*?)</h5>', line):
        extract(m.group(1), 'h5', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h6 (.*?)>(.*?)</h6>', line):
        extract(m.group(1), 'h6', m.group(2), m.group(3))

    elif m := re.match(r'(\s*)<h1>(.*?)</h1>', line):
        extract(m.group(1), 'h1', '', m.group(2))

    elif m := re.match(r'(\s*)<h2 (.*?)>$', line):
        extract(m.group(1), 'h2', m.group(2))
        
    elif m := re.match(r'(\s*)<ul (.*?)>$', line):
        extract(m.group(1), 'ul', m.group(2))
        
    elif m := re.match(r'(\s*)<p>(.*?)</p>', line):
        extract(m.group(1), 'p', '', m.group(2))

    elif m := re.match(r'(\s*)<p (.*?)>$', line):
        extract(m.group(1), 'p', m.group(2))

    elif m := re.match(r'(\s*)<button (.*?)>(.*?)</button>', line):
        extract(m.group(1), 'button', m.group(2), m.group(3))
        
    elif m := re.match(r'(\s*)<button (.*?)>$', line):
        extract(m.group(1), 'button', m.group(2))

    elif m := re.match(r'(\s*)<img (.*?)/?>$', line):
        extract(m.group(1), 'img', m.group(2))

    elif m := re.match(r'(\s*)<label (.*?)>$', line):
        extract(m.group(1), 'label', m.group(2))

    elif m := re.match(r'(\s*)<input (.*?)/?>$', line):
        extract(m.group(1), 'input', m.group(2))

    elif m := re.match(r'(\s*)<section (.*?)>$', line):
        extract(m.group(1), 'section', m.group(2))

    elif m := re.match(r'(\s*)<article (.*?)>$', line):
        extract(m.group(1), 'article', m.group(2))

    elif m := re.match(r'(\s*)<li>(.*?)</li>', line):
        print(f"{m.group(1)}li {m.group(2)}")

    elif m := re.match(r'(\s*)<li>$', line):
        print(f"{m.group(1)}li")

    elif m := re.match(r'(\s*)<p>$', line):
        print(f"{m.group(1)}p")

    elif m := re.match(r'(\s*)</', line):
        pass

    elif m := re.match(r'(\s*)<', line):
        print("GAH", repr(line))
        exit(2)

    elif m := re.match(r'(\s*)(.*)$', line):
        print(f"{m.group(1)}|{m.group(2)}")
        
    else:
        print("ZZZ")
        exit(99)
