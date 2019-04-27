#!python3
# !/usr/bin/python
# -*- coding: utf-8 -*-
# Para limpiar el json general obtenido del repositorio

fname = input("Enter a file name: ")
# do it also with 1-bundesliga-ii.txt
if (len(fname) < 1):
    fname = '1-bundesliga.txt'

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

fh.write(news)
# print news

fh.close()
