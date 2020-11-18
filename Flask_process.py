# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:37:34 2020

@author: khlifi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
from flask import render_template

app = Flask(__name__)


colors = ['red', 'yellow', 'green', 'orange','dark','magenta','cyan','blue']
numbers=[1,2,3,4,5,6,7,8,9,10]
@app.route('/', methods=['GET','POST'])

def home():
  
    return render_template(
        'Home.html',numbers=numbers,colors=colors)

@app.route("/Process" , methods=['GET', 'POST'])
def process():
   
    color=""
    number=""
    if (request.method == 'POST'):
       color = request.form.get('color')
       number = request.form.get('number')
  
    process_list=[]
    for i in range(int(number)):
        process_list.append(color)
    return render_template(
        'Process.html',colors=colors,numbers=numbers,process_list=process_list)
if __name__ == "__main__":
    app.run()