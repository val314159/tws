import os, sys

for line in sys.stdin:
    if 'site.css' in line:
        print(f"""<style>{
            open('docs/site.css').read()
        }</style>""")
    else:
        print(line, end='')
    pass
