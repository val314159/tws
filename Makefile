call:: clean tree all
all:: build serve
build:: node_modules
	tailwind -mo docs/site.css
	python filter.py <docs/index.html >docs/i.html
	wc docs/index.html docs/i.html
node_modules: package.json ; bun i
serve::;python -mhttp.server 80
_clean:: clean tree
realclean:: clean
	rm -fr auto-save-list
	rm -fr __pycache__ node_modules
	rm -fr yarn.lock bun.lockb package-lock.json
	find . -name '\#*\#' -o -name '.\#*' | xargs rm -fr
clean::
	rm -fr docs/site.css
	find . -name '*~' -o -name '.*~' | xargs rm -fr
T=-I .git -I node_modules -I __pycache__
tree:;	tree $T -a

