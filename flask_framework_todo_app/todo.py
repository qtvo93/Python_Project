# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:24:18 2020

@author: Thinh Vo
"""

from flask import Flask 
app = Flask(__name__) 
  
@app.route('/hello/<name>') 
def hello_name(name): 
   return 'Hello %s!' % name 
  
if __name__ == '__main__': 
   app.run() 