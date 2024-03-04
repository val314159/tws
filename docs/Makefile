call:: clean all
all:: i2.html i3.html
xxxi2.html: i2.pug.html
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
%.html: %.pug.html
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
i2.pug.html: index2.html
	./f.py  $^ >$@
clean:: ; rm -fr i2.pug.html i2.html i3.html *~
