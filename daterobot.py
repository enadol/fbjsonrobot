# !python3
import re
# import time
from fbjson import lstdate
# from jsonbuilderbis import match

lstdatenew = []
lstnuevafecha = []
for item in lstdate:
	#regex para extraer p.e. 
	corte = re.compile('.*\s(.*)]')
	#print(lstdate)
	nada, fecha, nada2 = corte.split(item)
	#print(fecha)
	#para fecha sin . p. ej [Fr ]
	#partida = fecha[0].split('  ')
	#print(partida)
	#dia = partida[1]
	
	#para fecha con . p. ej [Fr. ]
	partida = fecha.split('.')
	dia = partida[0].zfill(2)
	#print(dia)
	
	mes = partida[1].zfill(2)
	#print(mes)
	
	if int(mes) >= 8:
		partida[2] = "2019"
		
		#print mes
	else:
		partida[2] = "2020"
	#print mes, fecha[2]
	separator="-"
	ffecha = separator.join([partida[2], mes, dia])

	#print(ffecha)
	#ddia = nuevafecha1[0]
	#mmes = nuevafecha1[1]
	#yyear = nuevafecha1[2]
	#ffecha = yyear + "-" + mmes + "-" + ddia
	#nuevafecha2=ddia+"-"+mmes+"-"+yyear
	#nuevafecha3=datetime.datetime.strptime(nuevafecha2, "%d-%m-%Y").strftime("%Y-%m-%d")
	lstnuevafecha.append(ffecha)
#print(lstnuevafecha)
	
	
