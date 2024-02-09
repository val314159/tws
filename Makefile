call:: clean tree all
all:: build serve
build::;tailwind -mo docs/site.css
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

