import re
#import urllib

#url=('https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt')
fh=open('1-bundesliga-i.txt')
clubcodes={"Eintracht Frankfurt": "FFM","1899 Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","Hamburger SV": "HSV","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","Werder Bremen": "BRE","Bor. Moenchengladbach":"BMG", "Bayer Leverkusen":"B04","1. FC Koeln":"KOE","FC Ingolstadt 04":"FCI","SV Darmstadt 98":"D98","FC Schalke 04":"S04","1. FSV Mainz 05":"M05"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "1899 Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","Hamburger SV":"hsv","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","Werder Bremen":"bremen","Bor. Moenchengladbach": "mgladbach","Bayer Leverkusen":"leverkusen","1. FC Koeln":"koeln","FC Ingolstadt 04":"ingolstadt","SV Darmstadt 98":"darmstadt","FC Schalke 04":"schalke","1. FSV Mainz 05":"mainz"}
lsthome=[]
lstaway=[]
lstgoalshome=[]
lstgoalsaway=[]
lstdate=[]
lstjornada=[]

for text in fh:
	line=text.rstrip()
	if line.startswith('['):
		date=line
		lstdate.append(date)
	
	if 'Jornada' in line:
		jornada=line
		#print jornada
		lstjornada.append(jornada)

	taway=re.compile('.*:.')
	thome=re.compile('.:.*')
	tghome=re.compile(':.*')
	tgaway=re.compile('.*:')
	#res=re.findall(r'^\s+.*\s.*', line)
	#print res
	roh=taway.split(line)
	roh2=thome.split(line)
	roh3=tghome.split(line)
	roh4=tgaway.split(line)

	#print roh4
	if len(roh3)>1:
		position=0
		item10=roh3[0]
		
		positionhome=len(item10)-1
		#print position
		goalshome=item10[positionhome:]
		lstgoalshome.append(goalshome)

		item11=roh4[1]
		goalsaway=item11[:1]
		lstgoalsaway.append(goalsaway)


	if len(roh2)>1:
		item=roh2[0]
		item2=item.split('  ',2)
		#split para quitar espacios
		item3=item2[2]
		#print item3
		item4=item3.split(' ',1)
		#print item4
		item5a=item4[1]
		#print item5a
		item6a=item5a.split('  ')
		teamhome=item6a[0].rstrip()
		#print teamhome
		lsthome.append(teamhome)
	else:
		continue

	if len(roh)>1:
		
		item5=roh[1]
		
		item6=item5.split('  ', 1)
		item7=item6[1]
		item8=item7.split(' ', 1)
		teamaway=item7.lstrip()
		#print teamaway
		lstaway.append(teamaway)
		
	else:
		continue
#print lstaway
# print lsthome
#print lstjornada
# print lstdate
# print lstgoalshome
# print lstgoalsaway
# print len(lstaway)
# print len(lsthome)
# print len(lstjornada)
# print len(lstdate)
# print len(lstgoalshome)
# print len(lstgoalsaway)