call:: clean all
all:: i2.html i3.html
%.html: %.html.pug
	cat $^ \
	| perl -npe 's!:!__COLON__!g' \
	| perl -npe 's!/!__SLASH__!g' \
	| perl -npe 's!\[!__OPEN___!g' \
	| perl -npe 's!\]!__CLOSE__!g' \
	| pypugjs \
	| perl -npe 's!__COLON__!:!g' \
	| perl -npe 's!__SLASH__!/!g' \
	| perl -npe 's!__OPEN___![!g' \
	| perl -npe 's!__CLOSE__!]!g' \
	>$@
i2.html.pug: index2.html
	./f.py  $^ >$@
clean:: ; rm -fr i2.html.pug i2.html i3.html *~
