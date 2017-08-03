from daterobot import lstnuevafecha
import datetime
import time

diadef=[]
#print lstnuevafecha
for date in lstnuevafecha:
	jornada=len(diadef)/9
	jornada +=1
	#print jornada
	#datelst=[]
	fecha=date.split('-')
	dia=fecha[0]
	mes=fecha[1]
	yyear=fecha[2]
	strdate=dia+','+mes+','+yyear
	for i in range(0, len(fecha)):
		date1=datetime.datetime.strptime(strdate, "%Y,%m,%d")
		date2=date1.strftime('%A')
	
	#only for season 2016/2017. MD on Easter Week. Delete or adjust for other seasons
	#if jornada == 29:
		#if date2=="Saturday":
			#for i in range(0,int(gamessaturday)):
				#diadef.append(date)
		#else:
			#for i in range(0,2):
				#diadef.append(date)
				
	#for the last two matchdays of each tournament,
	#all matches in one day
	# to be verified at the end of this tournament
	elif jornada>32:
		for i in range(0,9):
			diadef.append(date)

	
	elif date2=="Friday":
		gamesfriday=raw_input("¿Cuántos partidos se jugaron el viernes?: ")
		for i in range(0,int(gamesfriday)):
		diadef.append(date)

	elif date2=="Saturday":
		gamessaturday=raw_input("¿Cuántos partidos se jugaron el sábado?: ")
		for i in range(0, int(gamessaturday)):
			diadef.append(date)
		
	elif date2=="Sunday":
		gamessunday=raw_input("¿Cuántos partidos se jugaron el domingo?: ")
		for i in range(0, int(gamessunday)):
			diadef.append(date)
			
	elif date2=="Monday":
		gamesmonday=raw_input("¿Cuántos partidos se jugaron el lunes?: ")
		for i in range(0, int(gamesmonday)):
			diadef.append(date)
		
	elif date2=="Tuesday":
		gamestuesday=raw_input("¿Cuántos partidos se jugaron el martes?: ")
		for i in range(0, int(gamestuesday)):
			diadef.append(date)
	
	elif date2=="Wednesday":
		gameswednesday=raw_input("¿Cuántos partidos se jugaron el miércoles?: ")
		for i in range(0, int(gameswednesday)):
			diadef.append(date)
	else:
		gamesthursday=raw_input("¿Cuántos partidos se jugaron el jueves?: ")
		for in in range (0, int(gamesthursday)):
			diadef.append(date)

	
	#for wednesday matches on english weeks
	#else:
		#for i in range(0,5):
			#diadef.append(date)
		

#print diadef
#print len(diadef)
