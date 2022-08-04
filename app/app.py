from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='static/none.png', href3='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        mybag = ''
        if str(myage) =='' or str(mygender) =='':
            return render_template('index.html', href2='static/none.png', href3='Please insert your age and gender.')
        else:
            model = load('app/readinghabit-recommander.jolib')
            np_arr = np.array([myage, mygender])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            
            if 'beauty' in predictions_to_str:
                mybag = 'static/beauty.jpg'
            elif 'business' in predictions_to_str:
                mybag = 'static/businnes.jpg'
            elif 'comic' in predictions_to_str:
                mybag = 'static/comic.jpg'
            elif 'fasion' in predictions_to_str:
                mybag = 'static/fasion.jpg'
            elif 'healthy-food' in predictions_to_str:
                mybag = 'static/healthy-food.jpg'
            else:
                mybag = 'static/none.png' 
                
            return render_template('index.html', href2=str(mybag), href3='The suitable bread for you (age:'+str(myage)+' ,gender:'+str(mygender)+') is:'+predictions_to_str)
        

