call:: clean tree all
all:: build serve
build:: node_modules
	tailwind -mo docs/site.css
	mkdir -p docs/x
	python filter.py <docs/index.html >docs/x/index.html
	wc docs/index.html docs/x/index.html
node_modules: package.json ; bun i
serve::;python -mhttp.server 80
clean:: clean tree
realclean:: clean
	rm -fr auto-save-list
	rm -fr __pycache__ node_modules
	rm -fr yarn.lock bun.lockb package-lock.json
	find . -name '\#*\#' -o -name '.\#*' | xargs rm -fr
clean::
	rm -fr docs/site.css docs/x
	find . -name '*~' -o -name '.*~' | xargs rm -fr
T=-I .git -I node_modules -I __pycache__
tree:;	tree $T -a

