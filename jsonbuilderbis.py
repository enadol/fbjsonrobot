from fbjsonbis import lstjornada
from fbjsonbis import lstdate
from fbjsonbis import lsthome
from fbjsonbis import lstaway
from fbjsonbis import lstgoalshome
from fbjsonbis import lstgoalsaway
from fbjsonbis import clubkeys
from fbjsonbis import clubcodes


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

def getkeyCodes(team, dict):
	equipo=dict[team]
	return equipo
	#return equipo



import re
# for season in seasons:
# season=
# for round in rondas:
#     round=
#print lstgoalsaway

for d in range(0,len(lstdate)):
	date=lstdate[d]
	#match.append(date)
  	#print len(lstdate)


#Jornada 1 a 34 o lo que vaya llenandose
#Jornada 1, etcetera
for b in range(0, len(lstjornada)):
    jornada=lstjornada[b]
    #print jornada


#nueve partidos de cada jornada
#for i in range(0,9):
		#name=lstpartidos[i]
		
		

for e in range(0,len(lsthome)):
	
	date="date"

	
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
	#lstteam1.append('**')
	#print len(lsthome)
	date1={"date": date}
	key14lst={'key': key1}
	name14lst={'name': name1}
	code14lst={'code': code1}

	key24list={'key': key2}
	name24lst={'name': name2}
	code24lst={'code': code2}
	#team1={'team1':[{'key': key1},{'name': name1},{'code': code1}]}
	#team2={'team2':[{'key': key2},{'name': name2},{'code': code2}]}
	score1={'score1': goals1}
	score2={'score2': goals2}
			
	
	# print date
	# print team1
	# print team2
	# print score1
	# print score2

	# print '\n'	
			
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
	#print len(lsthome)
#print matches

#match.append(lstteam2)
		#match.append(score1)
		#match.append(score2)
			#print score1
			#print score2

#matches.append(match)