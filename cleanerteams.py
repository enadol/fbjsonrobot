  #!/usr/bin/python
  # -*- coding: utf-8 -*-

#Para limpiar el json general obtenido del repositorio

fname = raw_input("Enter a file name: ")
#do it also with 1-bundesliga-ii.txt
if ( len(fname) < 1 ) : fname = 'bundesliga2017.txt'

fh = open(fname)
stringdata=fh.read()

fh=open(fname, "w")
news=stringdata.replace("ö", "oe")
stringdata=news
news=stringdata.replace("ü", "ue")
stringdata=news

fh.write(news)
	
#print news



fh.close()
