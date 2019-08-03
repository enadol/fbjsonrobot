# fbjsonrobot
## A Python robot that converts bundesliga .txt files from @geraldb ' s openfootball into JSON with the required structure.

Scripts with dependencies

Launch file is launch.py

Result file is bl.json

Requires Python 3.x. In Windows shell just enter "py launch.py", matchday and file name

## But first, check and/or adapt the code according to your needs (league, file names, paths, etc)

## NEW (08.2019): Access through url to the raw .txt file (https://raw.githubusercontent.com/openfootball/de-deutschland/master/2019-20/1-bundesliga.txt), thus no need to download 1.bundesliga.txt anymore. Script createtext.py generates a new .txt file (core.txt) with cumulative, dynamic output depending on the MD's advance. core.txt is now used to generate bundesliga.json, and...

## * JSOn output is now "pretty printed"

## ADDED: Dynamically finds ALL the different structures of MDs, due to changes in the Bundesliga starting season 2017/2018

## The scripts rely COMPLETELY AND VERY RIGIDLY on the format of the .txt file. Number of spaces and ":"s or "-"s declared on fbjson.py must be monitored and, if necessary, adjusted, for the regexes to work properly (currently they are OK). In this sense, flexibility is another task to achieve on this project.

## Scripts now in Python 3.x
