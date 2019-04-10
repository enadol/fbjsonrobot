#!python3
import re
from dateproofer import diadef
from fbjson import lstjornada
from fbjson import lstdate
from fbjson import lsthome
from fbjson import lstaway
from fbjson import lstgoalshome
from fbjson import lstgoalsaway
from fbjson import clubkeys
from fbjson import clubcodes


#print len(diadef) = 114
#print clubcodes
lstpartidos = []
matches = []
lstteam1 = []
lstteam2 = []
lstteams = []
ronda1 = []
ronda2 = []
rondas = [ronda1, ronda2]
match = []
count = 0
#print lsthome
#print len(lsthome) = 153
for e in range(0,len(lsthome)):
	#dinamically generated date from dateproofer.py
	date = diadef[e]
	name1 = lsthome[e]
	#print name1
	key1 = clubkeys[name1]
	#print key1
	code1 = clubcodes[name1]
	name2 = lstaway[e]
	key2 = clubkeys[name2]
	code2 = clubcodes[name2]
	goals1 = lstgoalshome[e]
	goals2 = lstgoalsaway[e]

	date1 = {"date": date}
	key14lst = {'key': key1}
	name14lst = {'name': name1}
	code14lst = {'code': code1}

	key24list = {'key': key2}
	name24lst = {'name': name2}
	code24lst = {'code': code2}
	score1 = {'score1': goals1}
	score2 = {'score2': goals2}
			
		
	match.append(date1)
	match.append(key14lst)
	match.append(name14lst)
	match.append(code14lst)
	match.append(key24list)
	match.append(name24lst)
	match.append(code24lst)
	match.append(score1)
	match.append(score2)
	matches.append(match)
#print match
#print diadef
