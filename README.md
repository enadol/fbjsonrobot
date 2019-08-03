# fbjsonrobot
## A Python robot that converts bundesliga .txt files from @geraldb ' s openfootball into JSON with the required structure.

Scripts with dependencies

Launch file is launch.py

Result file is bl.json

Requires Python 3.x. In Windows shell just enter "py launch.py", matchday and file name

## But first, check and/or adapt the code according to your needs (league, file names, paths, etc)

NEW (08.2019): Access through url to the raw .txt file. Script createtext.py generates a new .txt file (core.txt) with cumulative input depending on the MD's advace. core.txt is the used to generate de json, and...

* JSOn output is now "pretty printed"

## ADDED: Dynamically finds ALL the different structures of MDs, due to changes in the Bundesliga starting season 2017/2018

## The scripts rely COMPLETELY AND VERY RIGIDLY on the format of the .txt file. Spaces and ":"s in this file must be adjusted or verified for the scripts to work properly. In this sense, flexibility is another task to achieve on this project.

## Scripts now in Python 3.x
