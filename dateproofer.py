#!python3
from daterobot import lstnuevafecha
#from input import jornada as lunes
import datetime
import time

diadef=[]

#for special matchdays with three matches on sunday, beginning season 2017/2018.
#Replace/check items in array every new season
specialMD = [7,9]
conlunes = [13,22,23,25]
english = [5,16]
sevenplustwo = [0]

#print lstnuevafecha
#print lunes
for date in lstnuevafecha:
	jornada = len(diadef)//9
	jornada +=1
	#print jornada
	#datelst=[]
	fecha = date.split('-')
	dia = fecha[0]
	mes = fecha[1]
	yyear = fecha[2]
	strdate = dia+','+mes+','+yyear

	for i in range(0, len(fecha)):
		date1 = datetime.datetime.strptime(strdate, "%Y,%m,%d")
		date2 = date1.strftime('%A')
		
#special matchdays with five matches on saturday, two on sunday, one on monday	
#no need to change this every season. just change items in conlunes


#TODO CHECAR COMPUTO DE FECHAS: ESTA FALLANDO CONLUNES Y QUIZA OTRAS ESPECIALES EN PYTHON 3.
	if jornada in conlunes:
		#print "Si es de la jornada"
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

	#for wednesday matches on english weeks
	elif jornada in english:
		if date2 == 'Tuesday':
			for i in range(0,4):
				diadef.append(date)
		if date2 == 'Wednesday':
			for i in range(0,5):
				diadef.append(date)

	#new MD model with seven days on sat + 2
	elif jornada in sevenplustwo:
		if date2 == 'Saturday':
			for i in range(0,7):
				diadef.append(date)
		if date2 == 'Sunday':
			for i in range(0,2):
				diadef.append(date)

		
#special matchdays with three matches on sunday, five on saturday
#no need to change this every season. just change items in specialMD
	
	elif jornada in specialMD:
		if date2 == "Friday":
			diadef.append(date)
			
		elif date2 == "Saturday":
			for i in range(0,5):
				diadef.append(date)

		else: 
			for i in range(0, 3):
				diadef.append(date)

#MD on Easter Week. Delete or adjust MD Number for other seasons
	#elif jornada == 28:
		#for i in range(0,6):
			#diadef.append(date)
				
#for the last two matchdays of each tournament,
#all matches in one day
# to be verified at the end of this tournament
	elif jornada>32:
		for i in range(0,9):
			diadef.append(date)


	else:
		if date2=="Friday":
			diadef.append(date)

		if date2=="Saturday":
			for i in range(0,6):
				diadef.append(date)
		
		if date2=="Sunday":
			for i in range(0,2):
				diadef.append(date)

#print diadef
#print len(diadef)
