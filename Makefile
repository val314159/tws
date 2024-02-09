call:: clean tree all
all:: build # serve
build:: node_modules docs/site.css dist
docs/site.css::;tailwind -mo docs/site.css
node_modules: package.json ; bun i
serve::;python -mhttp.server 80
clean:: clean tree
realclean:: clean
	rm -fr auto-save-list dist docs/dist __pycache__
	rm -fr yarn.lock bun.lockb package-lock.json node_modules
	find . -name '\#*\#' -o -name '.\#*' | xargs rm -fr
clean::
	rm -fr docs/site.css docs/x
	find . -name '*~' -o -name '.*~' | xargs rm -fr
T=-I .git -I node_modules -I __pycache__
tree:;	tree $T -a
dist:
	cd docs ; rm   -fr x
	cd docs ; mkdir -p x
	cd docs ; ../filter.py index.html x/index.html
	cd docs ; wc index.html x/index.html
