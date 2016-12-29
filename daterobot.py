import datetime
import time
from fbjsonbis import lstdate
#from jsonbuilderbis import match

lstdatenew=[]
lstnuevafecha=[]
for item in lstdate:
	fecha=item.split('.')
	partida=fecha[0].split(' ')
	dia=partida[1]
	#print dia
	mes=str(fecha[1]).zfill(2)
	#print mes
	
	if mes>=8:
		fecha[2]="2016"
		
		#print mes
	else:
		fecha[2]="2017"
	
	nuevafecha1=dia, mes, fecha[2]

	ddia=nuevafecha1[0]
	mmes=nuevafecha1[1]
	yyear=nuevafecha1[2]
	nuevafecha2=ddia+"-"+mmes+"-"+yyear
	nuevafecha3=datetime.datetime.strptime(nuevafecha2, "%d-%m-%Y").strftime("%d-%m-%Y")
	lstnuevafecha.append(nuevafecha3)
#print lstnuevafecha
	
	