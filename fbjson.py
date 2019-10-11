#!/usr/bin/env python
# coding: utf-8
import re
from prelaunch import lstfechas as lstdate
from prelaunch import lstmd as lstjornada

fh = open("core.txt")

clubcodes={"Eintracht Frankfurt": "FFM","TSG Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","Werder Bremen": "BRE","Bor. Moenchengladbach":"BMG", "Bayer 04 Leverkusen":"B04","FC Schalke 04":"S04","1. FSV Mainz 05":"M05", "Fortuna Duesseldorf": "F95", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "TSG Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","Werder Bremen":"bremen","Bor. Moenchengladbach": "mgladbach","Bayer 04 Leverkusen":"leverkusen","FC Schalke 04":"schalke","1. FSV Mainz 05":"mainz", "Fortuna Duesseldorf": "duesseldorf", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "SC Paderborn 07": "SCP"}
lsthome=[]
lstaway=[]
lstgoalshome=[]
lstgoalsaway=[]
#lstdate=[]
lstjornada=[]




for text in fh:

    line = text.splitlines()
    #print(line)
    if line[0].startswith('['):
        date = line
        
    
    elif line[0].startswith('Spieltag'):
        mday = line
        #print(mday)
    #print(line[0])
    else:
        thome = re.compile(r'.{2}(.*)\b\s{3,}')
        taway = re.compile(r'.*-\d\s(.*)')
        tghome = re.compile(r'(.)-.*$')
        tgaway = re.compile(r'.*-(.)')

            
        teamhome = thome.split(line[0])[1]
        lsthome.append(teamhome)

       
        teamaway = taway.split(line[0])[1]
        lstaway.append(teamaway)

       
        goalshome = tghome.split(line[0])[1]
        lstgoalshome.append(goalshome)
     
        goalsaway = tgaway.split(line[0])[1]
        lstgoalsaway.append(goalsaway)
