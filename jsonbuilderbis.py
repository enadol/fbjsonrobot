import re
from dateproofer import diadef
from fbjsonbis import lstjornada
from fbjsonbis import lstdate
from fbjsonbis import lsthome
from fbjsonbis import lstaway
from fbjsonbis import lstgoalshome
from fbjsonbis import lstgoalsaway
from fbjsonbis import clubkeys
from fbjsonbis import clubcodes


#print diadef
lstpartidos=[]
matches=[]
lstteam1=[]
lstteam2=[]
lstteams=[]
ronda1=[]
ronda2=[]
rondas=[ronda1, ronda2]
match=[]
count=0

for e in range(0,len(lsthome)):
	#fecha dinamica desde dateproofer.py
	date=diadef[e]
	name1=lsthome[e]
	#print name1
	key1=clubkeys[name1]
	code1=clubcodes[name1]
	name2=lstaway[e]
	key2=clubkeys[name2]
	code2=clubcodes[name2]
	lstteam1.append(key1)
	lstteam1.append(name1)
	lstteam1.append(code1)
	goals1=lstgoalshome[e]
	
			#print lstteam1
			
	lstteam1.append(date)
	lstteam1.append(key2)
	lstteam1.append(name2)
	lstteam1.append(code2)
	goals2=lstgoalsaway[e]
	lstteam1.append(goals1)
	lstteam1.append(goals2)

	date1={"date": date}
	key14lst={'key': key1}
	name14lst={'name': name1}
	code14lst={'code': code1}

	key24list={'key': key2}
	name24lst={'name': name2}
	code24lst={'code': code2}
	score1={'score1': goals1}
	score2={'score2': goals2}
			
		
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
#print diadef
