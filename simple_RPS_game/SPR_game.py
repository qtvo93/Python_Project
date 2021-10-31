# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:32:29 2020

@author: Thinh Vo
"""

import random


def strategy(history):
    if not history: return random.choice(['R','P','S'])
        
    else:
        
        Play = [game[-1] for game in history]
        
        rP,rS,rR= Play.count('P'),Play.count('S'),Play.count('R')
        fP, fS,fR = rP/ len(Play), rS/ len(Play), rR/ len(Play)
              
        
        if fP >= 0.6 : 
            return 'S'
        elif fS >= 0.6 : 
            return 'R'
        elif fR >= 0.6 : 
            return 'P'
        else:
            return random.choices(['P', 'S', 'R'], [fR, fP, fS])[0]
        
        
history1=[]
choice=input("Enter your choice R/S/P-- Q to quit: \n" )  
while choice != 'Q':
    choice=input("Enter your choice R/S/P-- Q to quit: \n" )
    history1.append(choice) 

#history1=history1[:-1]    
   
print("player: ", random.choices(history1))
print("my robot: ", strategy(history1))
