from fbjsonbis import lstjornada
from fbjsonbis import lstdate
from fbjsonbis import lsthome
from fbjsonbis import lstaway
from fbjsonbis import lstgoalshome
from fbjsonbis import lstgoalsaway

import re
# for season in seasons:
# season=
# for round in rondas:
#     round=
#print lstgoalsaway
for b in range(0, len(lstjornada)):
  jornada=lstjornada[b]
#print jornada
    
for d in range(0,len(lstdate)):
  date=lstdate[d]
  print date

for e in range(0,len(lsthome)):
	team1=lsthome[e]
	team2=lstaway[e]
	score1=lstgoalshome[e]
	score2=lstgoalsaway[e]

#print date, team1, team2, score1, score2

#print match, date, team1, team2, score1, score2