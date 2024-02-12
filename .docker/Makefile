#D=--rm -it -v`pwd`:/root -p5173:5173 --network=host
D=--rm -it -v`pwd`:/root --network=host
T=dev
all::
	docker build . -t$T
#	docker   run  $D $T
