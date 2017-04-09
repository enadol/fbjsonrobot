# fbjsonrobot
## A Python robot that transforms bundesliga text files from @geraldb ' s openfootball and emulates its JSON using the required structure.

Scripts with dependencies

Launch file is launch.py

In Windows console python launch.py and the JSON file is generated

## But first, check and/or adapt the code according to your needs (league, file names, paths, etc)

This example uses 1-bundesliga-i.txt as origin file but can be adapted to use the raw github Link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt to it

The currently generated file (in this example, bundesliga.json) is intented to be used in spanish with UTF-8

TODO:

* JSOn is still to be "pretty printed"

* A future version in german is intented, to be used with the original JSON and the link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt

## The scripts rely COMPLETELY AND VERY RIGIDLY on the format of the .txt file. Spaces and ":"s in this file must be adjusted or verified for the scripts to work properly. In this sense, flexibility is another task to achieve on this project.

New scripts were integrated in order to dinamically generate the dates.
