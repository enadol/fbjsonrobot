# fbjsonrobot
A Python robot that transforms bundesliga text files from @geraldb ' s openfootball in JSON using the required structure.

Scripts with dependencies

Launch file is jsonrobot2.py

In Windows console python jsonrobot2.py and the JSON file is generated

Uses 1-bundesliga-i.txt as origin file but can be adapted to use the raw github Link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt to it

The currently generated file is intented to be used in spanish with UTF-8

TODO:

* The generated JSON bundesliga.json is still imperfect, but workable. At the end it still generates an unnecesary ",
{
 "name": "14. Jornada",

"matches": [
{"

to be substituted with "] }"

to result in a validated json

* JSOn is still to be "pretty printed"

* A future version in german is intented, to be used with the original JSON and the link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt

:important: The scripts rely heavily, no, completely and very rigidly on the format of the .txt file. Spaces and :s in this file must be adjusted or verified for the scripts to work properly. In this sense, flexibility is another task to achieve on this project.

Also, I'm still working to find out a way to make the dates in using the info on the .txt file
