grafalbum.pdf: grafalbum.py datos.txt
	python grafalbum.py

datos.txt: album
	./album > datos.txt

album: album.cpp
	c++ album.cpp -o album

