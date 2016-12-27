from daterobot import lstnuevafecha
import datetime
import time

#print lstnuevafecha
diadef=[]
for date in lstnuevafecha:
	datelst=[]
	fecha=date.split('-')
	dia=fecha[0]
	mes=fecha[1]
	yyear=fecha[2]
	strdate=dia+','+mes+','+yyear
	for i in range(0, len(fecha)):
		#fecha2=fecha[i]
		date1=datetime.datetime.strptime(strdate, "%d,%m,%Y")
		date2=date1.strftime('%A')
	if date2=="Friday":
		diadef.append(date)
	elif date2=="Saturday":
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
	elif date2=="Sunday":
		diadef.append(date)
		diadef.append(date)
	elif date2=="Tuesday":
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		
	else:
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)
		diadef.append(date)

#print diadef
#print len(diadef)

