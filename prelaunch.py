#!/usr/bin/env python
# coding: utf-8

import datetime
import re
import urllib.request

lstfechas = []
lstmd = []
hoy = datetime.datetime.now()
corte = re.compile('.*\s(.*)]')

with urllib.request.urlopen('https://raw.githubusercontent.com/openfootball/de-deutschland/master/2019-20/1-bundesliga.txt') as response:
    data = response.read()

    data2 = data.decode('utf-8')

    lines = data2.splitlines()



for line in lines:
    if line.startswith('Spieltag'):
        md = line
        #print(jornada)
    
    if line.startswith('['):
        fecha = line
        fecha = corte.split(fecha)
        fecha = fecha[1]
        dia, mes, nada = fecha.split('.')
        #print(mes)
        mes = mes.zfill(2)
        

       
        if int(mes) >= 8:
            year = 2019
        else:
            year = 2020
    
        date = datetime.datetime(year,int(mes),int(dia))
        #print(date)
    
        if date <= hoy:
            lstfechas.append(date)
            if md not in lstmd:
                lstmd.append(md)
                

jornada = len(lstmd)

