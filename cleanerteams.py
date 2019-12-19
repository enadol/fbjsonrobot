#!python3
# !/usr/bin/python
# -*- coding: utf-8 -*-
# Para limpiar el json general obtenido del repositorio

fname = input("Enter a file name: ")
# do it also with 1-bundesliga-ii.txt
if (len(fname) < 1):
    fname = 'https://raw.githubusercontent.com/openfootball/de-deutschland/master/2019-20/1-bundesliga.txt'

fh = open(fname)
stringdata = fh.read()

fh = open(fname, "w")
news = stringdata.replace("ö", "oe")
stringdata = news
news = stringdata.replace("ü", "ue")
stringdata = news
news = stringdata.replace("Ã¶", "oe")
stringdata = news
news = stringdata.replace("Ã¼", "ue")
stringdata = news
news = stringdata.replace("\\xc3\\xb6", "oe")
stringdata = news
news = stringdata.replace("\\xc3\\xbc", "ue")
stringdata = news

fh.write(news)
# print news

fh.close()
