#!/usr/bin/env python

import re, os, sys

for line in sys.stdin:

    line = line.replace('\t',' '*8)
    
    #print("L", line, end='')
    if   m := re.match(r'(\s*)$', line):

        #print()
        #print('Q', line, end='')
        pass
    
    elif m := re.match(r'(\s*)<!--', line):
        #print()
        pass
    
    elif m := re.match(r'(\s*)<!', line):
        print("!!!5")
        #print("doctype html")

    elif m := re.match(r'(\s*)<html (.*?)>', line):
        print(f"html({m.group(2)})")

    elif m := re.match(r'(\s*)<hr\s*/?>', line):
        print(f"{m.group(1)}hr")

    elif m := re.match(r'(\s*)<(meta|x?link) (.*?)/?>', line):
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
        print(f"{m.group(1)}footer({m.group(2)})")

    elif m := re.match(r'(\s*)<div (.*?)>(.*?)</div>', line):
        print(f"{m.group(1)}div({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<div (.*?)>$', line):
        print(f"{m.group(1)}div({m.group(2)})")

    elif m := re.match(r'(\s*)<div (.*?)>(.*?)', line):
        nope
        print(f"{m.group(1)}div({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<svg (.*?)>(.*?)</svg>', line):
        print(f"{m.group(1)}svg({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<a (.*?)>(.*?)</a>', line):
        print(f"{m.group(1)}a({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<time (.*?)>(.*?)</time>', line):
        print(f"{m.group(1)}time({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<span (.*?)>(.*?)</span>', line):
        print(f"{m.group(1)}span({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<span (.*?)>$', line):
        print(f"{m.group(1)}span({m.group(2)})")

    elif m := re.match(r'(\s*)<figure>(.*?)</figure>', line):
        print(f"{m.group(1)}figure {m.group(2)}")

    elif m := re.match(r'(\s*)<h1 (.*?)>(.*?)</h1>', line):
        print(f"{m.group(1)}h1({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h2 (.*?)>(.*?)</h2>', line):
        print(f"{m.group(1)}h2({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h3 (.*?)>(.*?)</h3>', line):
        print(f"{m.group(1)}h3({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h4 (.*?)>(.*?)</h4>', line):
        print(f"{m.group(1)}h4({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h5 (.*?)>(.*?)</h5>', line):
        print(f"{m.group(1)}h5({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h6 (.*?)>(.*?)</h6>', line):
        print(f"{m.group(1)}h6({m.group(2)}) {m.group(3)}")

    elif m := re.match(r'(\s*)<h1>(.*?)</h1>', line):
        print(f"{m.group(1)}h1 {m.group(2)}")

    elif m := re.match(r'(\s*)<h2 (.*?)>$', line):
        print(f"{m.group(1)}h2({m.group(2)})")
        
    elif m := re.match(r'(\s*)<ul (.*?)>$', line):
        print(f"{m.group(1)}ul({m.group(2)})")
        
    elif m := re.match(r'(\s*)<p>(.*?)</p>', line):
        print(f"{m.group(1)}p {m.group(2)}")

    elif m := re.match(r'(\s*)<p (.*?)>$', line):
        print(f"{m.group(1)}p({m.group(2)})")

    elif m := re.match(r'(\s*)<button (.*?)>(.*?)</button>', line):
        print(f"{m.group(1)}button({m.group(2)}) {m.group(3)}")
        
    elif m := re.match(r'(\s*)<button (.*?)>$', line):
        print(f"{m.group(1)}button({m.group(2)})")

    elif m := re.match(r'(\s*)<img (.*?)>$', line):
        print(f"{m.group(1)}img({m.group(2)})")

    elif m := re.match(r'(\s*)<label (.*?)>$', line):
        print(f"{m.group(1)}label({m.group(2)})")

    elif m := re.match(r'(\s*)<input (.*?)>$', line):
        print(f"{m.group(1)}input({m.group(2)})")

    elif m := re.match(r'(\s*)<section (.*?)>$', line):
        print(f"{m.group(1)}section({m.group(2)})")

    elif m := re.match(r'(\s*)<article (.*?)>$', line):
        print(f"{m.group(1)}article({m.group(2)})")

    elif m := re.match(r'(\s*)<li>(.*?)</li>', line):
        print(f"{m.group(1)}li {m.group(2)}")

    elif m := re.match(r'(\s*)<li>$', line):
        print(f"{m.group(1)}li")

    elif m := re.match(r'(\s*)<p>$', line):
        print(f"{m.group(1)}p")

    elif m := re.match(r'(\s*)</', line):
        #print()
        pass

    elif m := re.match(r'(\s*)<', line):
        print("GAH", repr(line))
        exit(2)

    elif m := re.match(r'(\s*)(.*)$', line):
        print(f"{m.group(1)}|{m.group(2)}")
        
    else:
        print("ZZZ")
        exit(99)
