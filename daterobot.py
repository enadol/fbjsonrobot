import datetime
import time
from fbjson import lstdate
#from jsonbuilderbis import match

lstdatenew=[]
lstnuevafecha=[]
for item in lstdate:
	fecha=item.split('.')
	#print fecha
	partida=fecha[0].split(' ')
	#print partida
	dia=partida[1]
	#print dia
	mes=fecha[1].zfill(2)
	#print int(fecha[1])
	
	if int(mes) >=8:
		fecha[2]="2017"
		
		#print mes
	else:
		fecha[2]="2018"
	#print mes, fecha[2]
	nuevafecha1=dia, mes, fecha[2]
	#print nuevafecha1
	ddia=nuevafecha1[0]
	mmes=nuevafecha1[1]
	yyear=nuevafecha1[2]
	nuevafecha2=ddia+"-"+mmes+"-"+yyear
	nuevafecha3=datetime.datetime.strptime(nuevafecha2, "%d-%m-%Y").strftime("%Y-%m-%d")
	lstnuevafecha.append(nuevafecha3)
#print lstnuevafecha
	
	
