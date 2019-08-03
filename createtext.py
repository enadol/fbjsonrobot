import urllib.request
from input import jornada

with urllib.request.urlopen('https://raw.githubusercontent.com/openfootball/de-deutschland/master/2019-20/1-bundesliga.txt') as response:
	data = response.read()

	data2 = data.decode('utf-8')

	filename = "core.txt"

	archivo = open(filename, "w", newline = '\n')

	data2 = data2.replace("ö", "oe")

	data2 = data2.replace("ü", "ue")

	lines = data2.splitlines()

count = 0

for line in lines:
	if line.startswith('Spieltag'):
		if count < jornada:
			count = count +1
			archivo.write(line)
			archivo.write('\n')
		else:
			break

	else:
		if count <= jornada:
			if line.startswith('[') or line.startswith(' ') or line.startswith('\n'):
				archivo.write(line)
				archivo.write('\n')
		else:
			break

archivo.close()