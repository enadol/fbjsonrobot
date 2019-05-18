import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/enadol/fbjsonrobot/master/bundesliga.json') as response:
	#print(response)
	data = response.read()
	#print(data)
	inp = 33
	outp = inp - 1
	js = json.loads(data)
	print(js['rounds'][outp])
