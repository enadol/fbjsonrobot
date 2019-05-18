from input import jornada as howmany
from jsonbuilder import match, score1, score2, lstjornada
import json
import pprint
from daterobot import lstnuevafecha

count = 0
countjuegos = 1
countteam = 2
countjornada = 0
pp = pprint.PrettyPrinter(indent=4)
# print score1, score2
fhand = open('bundesliga.json', 'w')
fhand.write('{\n"name": "Deutsche Bundesliga 2018/19",\n"rounds": [\n{\n"name": "1. Jornada",\n"matches": [\n{\n')
#print match[501]

for item in match:
	count = count+1
	llaves = list(item.keys())
	valores = list(item.values())
	llaves1 = llaves[0]
	valores1 = valores[0]

	for key in item:

		if llaves1 =='score1' or llaves1 == 'score2':
			fhand.write('"' + llaves1 +'" : '+ valores1)
		else: 
			fhand.write('"' + llaves1 + '" : "' + valores1 + '"')

		if llaves1 == 'date':
			fhand.write(',\n"team1": {\n')
		
		if llaves1 == 'code':
			fhand.write('\n},\n')
			if countteam%2 == 0:
		    		fhand.write('"team2": \n{\n')
			countteam = countteam+1
		else:
			if llaves1 != 'score2':
				if llaves1 != 'date':
					fhand.write(',\n')
				else:
					continue

		if llaves1 == 'score2':
			if countjuegos%9 == 0:
				if count < len(match):
					fhand.write('\n}\n]\n},\n{')
					countjuegos == 1
				else:
					fhand.write('\n}\n]\n}')
			else:
			
				fhand.write('\n},\n{\n')
		
		else:
			continue
		countjuegos +=1
			
	if (count % 81 == 0):
		jornada = (count/81)
		#to avoid printing the last, empty md
		#md * 10. factor chosen alleatory
		lstjornada.append(jornada)
		countjornada = jornada * 10
		#TODO: dinamically generate factor

		if countjornada < int(howmany) * 10:

			fhand.write('\n "name": "'+str(int(jornada+1))+'. Jornada",\n')
			fhand.write('\n"matches": [\n{\n')

		else:
			fhand.write('\n]\n}')
	else:
		continue



#print count

fhand.close()
