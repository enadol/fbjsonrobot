#!/usr/bin/env python
# coding: utf-8
import re
fh = open("core.txt", 'r')

clubcodes={"Eintracht Frankfurt": "FFM","TSG Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","Werder Bremen": "BRE","Bor. Moenchengladbach":"BMG", "Bayer 04 Leverkusen":"B04","FC Schalke 04":"S04","1. FSV Mainz 05":"M05", "Fortuna Duesseldorf": "F95", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "TSG Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","Werder Bremen":"bremen","Bor. Moenchengladbach": "mgladbach","Bayer 04 Leverkusen":"leverkusen","FC Schalke 04":"schalke","1. FSV Mainz 05":"mainz", "Fortuna Duesseldorf": "duesseldorf", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
lsthome=[]
lstaway=[]
lstgoalshome=[]
lstgoalsaway=[]
lstdate=[]
lstjornada=[]

thome = re.compile('.{2}(.*)\s{3,}')
taway = re.compile('.*\d-\d\s(.*)')
tghome = re.compile('^\D*(.).*$')
tgaway = re.compile('.*-(.)')


for text in fh:
    line = text.rstrip()
    
    if line.startswith('['):
        date = line
        lstdate.append(date)
    
    elif 'Spieltag' in line:
        jornada = line
        lstjornada.append(jornada)
        
    else:
        linea = line
        teamhome = thome.split(linea)[1]
        teamhome = teamhome.rstrip()
        lsthome.append(teamhome)
        #print(teamhome)
        
        teamaway = taway.split(linea)[1]
        lstaway.append(teamaway)
        #print(teamaway)
        
        goalshome = tghome.split(linea)[1]
        lstgoalshome.append(goalshome)
        
        goalsaway = tgaway.split(linea)[1]
        lstgoalsaway.append(goalsaway)

        

print(lsthome)
print(lstaway)

