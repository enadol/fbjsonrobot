import re
#initial script. cleans data from .txt
#to open the two files of the season (rounds) use-uncomment merger.py and bundesliga2017.txt

#url=('https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt')
fh=open('core.txt')
#print fh
clubcodes={"Eintracht Frankfurt": "FFM","TSG Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","Werder Bremen": "BRE","Bor. Moenchengladbach":"BMG", "Bayer 04 Leverkusen":"B04","FC Schalke 04":"S04","1. FSV Mainz 05":"M05", "Fortuna Duesseldorf": "F95", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "TSG Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","Werder Bremen":"bremen","Bor. Moenchengladbach": "mgladbach","Bayer 04 Leverkusen":"leverkusen","FC Schalke 04":"schalke","1. FSV Mainz 05":"mainz", "Fortuna Duesseldorf": "duesseldorf", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
lsthome=[]
lstaway=[]
lstgoalshome=[]
lstgoalsaway=[]
lstdate=[]
lstjornada=[]

for text in fh:
	line=text.rstrip()
	#print line
	if line.startswith('['):
		date=line
		lstdate.append(date)
		
	if 'Spieltag' in line:
		jornada=line
		#print jornada
		lstjornada.append(jornada)

	taway=re.compile('.*-.')
	thome=re.compile('.-.*')
	tghome=re.compile('-.*')
	tgaway=re.compile('.*-')
	tspaces=re.compile('\s{2}')
	
	roh=taway.split(line)
	roh2=thome.split(line)
	roh3=tghome.split(line)
	roh4=tgaway.split(line)
	#print roh3

	#print roh2[0]
	if len(roh3)>1:
		position=0
		item10=roh3[0]
		#print item10
		positionhome=len(item10)-1
		#print position
		goalshome=item10[positionhome:]
		#print goalshome
		lstgoalshome.append(goalshome)
		#print lstgoalshome
		item11=roh4[1]
		goalsaway=item11[:1]
		#print goalsaway
		lstgoalsaway.append(goalsaway)


	if len(roh2)>1:
		item = roh2[0]
		#print item.strip()
		item2 = item.split('  ',2)
		#PRUEBA si no funciona, quitar y poner linea 59 original
		#item2 = tspaces.split(item ,2)
		#print item2
		#split para quitar espacios
		item3 = item2[1]
		#print item3
		teamhome = item3.strip()
		#print teamhome
		lsthome.append(teamhome)
		#print lsthome
	else:
		#print "Lista vacia"
		continue

	if len(roh)>1:
		
		item5=roh[1]
		teamaway=item5.strip()
		lstaway.append(teamaway)
		#print teamaway
	else:
		continue

#print lstjornada
#print lstdate
#print lsthome