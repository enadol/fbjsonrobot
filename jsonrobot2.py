from jsonbuilderbis import match, score1, score2, lstjornada
import json
import pprint

count=0
countjuegos=1
countteam=2
#print score1, score2
fhand=open('bundesliga.json', 'w')
fhand.write('{\n"name": "Deutsche Bundesliga 2016/17",\n"rounds": [\n{\n"name": "1. Jornada",\n"matches": [\n{\n')
#print match[501]

for item in match:
	count =count+1
	llaves=item.keys()
	valores=item.values()
	llaves1=llaves[0]
	valores1=valores[0]
	#fhand.write('{')
	for key in item:
		fhand.write('"'+llaves1+'" : "'+valores1+'"')
		if llaves1=='date':
			fhand.write(',\n"team1": {\n')

		
		if llaves1=='code':
			fhand.write('\n},\n')
			if countteam%2==0:
		    		fhand.write('"team2": \n{\n')
			countteam=countteam+1
		else:
			if llaves1!='score2':
				if llaves1!='date':
					fhand.write(',\n')
				else:
					continue
		
		
			#print countjuegos

	#defi=valores[0]


		if llaves1=='score2':
			if countjuegos%9==0:
				fhand.write('\n}\n]\n},\n{')
				countjuegos==1
			else:
				fhand.write('\n},\n{')
		
		else:
			continue
		countjuegos +=1
			

	if (count%81==0):
		jornada=(count/81)
		fhand.write('\n "name": "'+str(jornada+1)+'. Jornada",\n')
		fhand.write('\n"matches": [\n{\n')

	else:
		continue


fhand.close()