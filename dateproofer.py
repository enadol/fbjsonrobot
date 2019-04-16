# !python3
from daterobot import lstnuevafecha
# from input import jornada as lunes
import datetime
# import time

diadef = []

# special matchday formats
# choose format array and append matchdays as items accordingly
# array items change every season
specialMD = [7, 9, 29, 32]
conlunes = [13, 22, 23, 25]
english = [5, 16]
sevenplustwo = [0]
sinviernes = [30]

# print lstnuevafecha
# print lunes
# len(diadef) must be == len(lsthome) == len(lstaway)
# SOLVED: operator // floor division instead of / por python 3.x
for date in lstnuevafecha:
	jornada = len(diadef) // 9
	jornada +=1
	#print jornada
	#datelst=[]
	fecha = date.split('-')
	dia = fecha[0]
	mes = fecha[1]
	yyear = fecha[2]
	strdate = dia+','+mes+','+yyear
# extract weekday of date using datetime, strftime
	for i in range(0, len(fecha)):
		date1 = datetime.datetime.strptime(strdate, "%Y,%m,%d")
		date2 = date1.strftime('%A')

# proof if machday is of special format

# matchdays with five matches on saturday, two on sunday, one on monday
# no need to change this every season. just change items in conlunes
# matchday with one match on monday
	if jornada in conlunes:
		if date2 == 'Friday':
			diadef.append(date)
		elif date2 == 'Saturday':
			for i in range(0,5):
				diadef.append(date)
		elif date2 == 'Sunday':
			for i in range(0,2):
				diadef.append(date)
		else: 
			if date2 == 'Monday':
				for i in range(0, 1):
					diadef.append(date)	

	# matchday on tuesday and wednesday
	elif jornada in english:
		if date2 == 'Tuesday':
			for i in range(0,4):
				diadef.append(date)
		if date2 == 'Wednesday':
			for i in range(0,5):
				diadef.append(date)

	# seven matches on sat + 2 sunday
	elif jornada in sevenplustwo:
		if date2 == 'Saturday':
			for i in range(0,7):
				diadef.append(date)
		if date2 == 'Sunday':
			for i in range(0,2):
				diadef.append(date)

		
# three matches on sunday, five on saturday, one friday
	elif jornada in specialMD:
		if date2 == "Friday":
			diadef.append(date)
			
		elif date2 == "Saturday":
			for i in range(0,5):
				diadef.append(date)

		else: 
			for i in range(0, 3):
				diadef.append(date)

# six matches on saturday, two sunday, one monday
	elif jornada in sinviernes:
		if date2 == "Saturday":
			for i in range(0,6):
				diadef.append(date)
		
		elif date2 == "Sunday":
			for i in range(0, 2):
				diadef.append(date)
		
		else:
			diadef.append(date)

# MD on Easter Week. Delete or adjust MD Number for other seasons
	# elif jornada == 28:
		# for i in range(0,6):
			# diadef.append(date)
				
# for the last two matchdays of each tournament,
# all matches in one day
	elif jornada > 32:
		for i in range(0, 9):
			diadef.append(date)

# if matchday is not special format, then traditional
# traditional matchdays: one friday, six saturday, two sunday
	else:
		if date2 == "Friday":
			diadef.append(date)

		if date2 == "Saturday":
			for i in range(0,6):
				diadef.append(date)
		
		if date2 == "Sunday":
			for i in range(0,2):
				diadef.append(date)

# print diadef
# print len(diadef)
