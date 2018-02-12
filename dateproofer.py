from daterobot import lstnuevafecha
import datetime
import time

diadef=[]

#for special matchdays with three matches on sunday, beginning season 2017/2018.
#Replace/check items in array every new season
specialMD=frozenset([4, 7, 9, 15])
conlunes=frozenset([23,26])

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
		
	#special matchdays with five matches on saturday, two on sunday, one on monday	
	if jornada in conlunes:
	    if date2=="Friday":
	        diadef.append(date)			
	    elif date2=="Saturday":
		for i in range(0,5):
		    diadef.append(date)
	    elif date2="Sunday":
		for i in range(0,2)
	    else: 
		for i in range(0, 1):
		    diadef.append(date)	
		
		
	#special matchdays with three matches on sunday, five on saturday
	#no need to change this every season. just change items in specialMD
	
	if jornada in specialMD:
	    if date2=="Friday":
	        diadef.append(date)
			
	    elif date2=="Saturday":
		for i in range(0,5):
		    diadef.append(date)
	    else: 
		for i in range(0, 3):
		    diadef.append(date)
			
	elif date2=="Friday":
		diadef.append(date)

	elif date2=="Saturday":
		for i in range(0,6):
		    diadef.append(date)
		
	elif date2=="Sunday":
		for i in range(0,2):
		    diadef.append(date)
		
	elif date2=="Tuesday":
		for i in range(0,4):
		    diadef.append(date)
			
	
			
	#only for season 2016/2017. MD on Easter Week. Delete or adjust for other seasons
	#elif jornada == 29:
		#for i in range(0,6):
			#diadef.append(date)
				
	#for the last two matchdays of each tournament,
	#all matches in one day
	# to be verified at the end of this tournament
	elif jornada>32:
		for i in range(0,9):
		    diadef.append(date)

	#for wednesday matches on english weeks
	else:
		for i in range(0,5):
		     diadef.append(date)
		

#print diadef
#print len(diadef)
