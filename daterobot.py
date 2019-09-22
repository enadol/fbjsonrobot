# !python3
import re
# import time
from fbjson import lstdate

lstdatenew = []
lstnuevafecha = []
for item in lstdate:
	#regex para extraer p.e. 
	corte = re.compile('.*\s(.*)]')
	
	nada, fecha, nada2 = corte.split(item)
	
	#para fecha con . p. ej [Fr. ]
	partida = fecha.split('.')
	dia = partida[0].zfill(2)
		
	mes = partida[1].zfill(2)
	
	if int(mes) >= 8:
		partida[2] = "2019"
	else:
		partida[2] = "2020"
	
	separator="-"
	ffecha = separator.join([partida[2], mes, dia])
	lstnuevafecha.append(ffecha)

	
	
