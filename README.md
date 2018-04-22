# fbjsonrobot
## A Python robot that encodes bundesliga .txt files from @geraldb ' s openfootball into JSON with the required structure.

Scripts with dependencies

Launch file is launch.py

Result file is bundesliga.json

In Windows shell just give python launch.py and ENTER for the JSON result file to be generated

## But first, check and/or adapt the code according to your needs (league, file names, paths, etc)

This example uses 1-bundesliga-i.txt as origin file but can be adapted to use the raw github Link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt to it

The currently generated file (in this example, bundesliga.json) is intented to be used in spanish with UTF-8

TODO:

* JSOn output is still to be "pretty printed" or indented

* A future version in german is intented, to be used with the original JSON and the link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt

## ADDED: Dynamically finds ALL the different structures of MDs, due to changes in the Bundesliga starting season 2017/2018

## The scripts rely COMPLETELY AND VERY RIGIDLY on the format of the .txt file. Spaces and ":"s in this file must be adjusted or verified for the scripts to work properly. In this sense, flexibility is another task to achieve on this project.
