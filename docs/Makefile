call:: clean all
all:: i2.html
#all:: i2.pug.html
i2.html: i2.pug.html
	pypugjs $^ | perl -npe 's!__COLON__!:!g;s!__SLASH__!/!g' >$@
i2.pug.html: index2.html
	./f.py  $^ >$@
clean:: ; rm -fr i2.pug.html i2.html *~
