call:: clean tree all
all:: build # serve
build:: node_modules docs/site.css dist
docs/site.css::;tailwind -mo docs/site.css
node_modules: package.json;bun i
serve::;python -mhttp.server 80
clean:: clean tree
realclean:: clean
	rm -fr auto-save-list dist docs/x __pycache__
	rm -fr yarn.lock bun.lockb package-lock.json node_modules
	find . -name '\#*\#' -o -name '.\#*' | xargs rm -fr
clean::
	rm -fr docs/site.css docs/dist
	find . -name '*~' -o -name '.*~' | xargs rm -fr
T=-I .git -I node_modules -I __pycache__
tree:;tree $T -a
dist:
	mkdir -p docs/x
	./filter.py -C docs ../src/index.html x/index.html --scripts
download::
	cd docs ; wget https://unpkg.com/htmx.org@1.9.10/dist/htmx.min.js
	cd docs ; wget https://unpkg.com/hyperscript.org@0.9.12/dist/_hyperscript.min.js
