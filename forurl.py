import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/openfootball/de-deutschland/master/2019-20/1-bundesliga.txt') as response:
	#print(response)
	data = response.read()
	#print(data)
	inp = 33
	outp = inp - 1
	js = json.loads(data)
	#print(js['rounds'][outp])
