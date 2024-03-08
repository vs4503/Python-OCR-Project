from flask import Flask
import datetime

date = datetime.datetime.now()

app = Flask(__name__)

@app.route('/data')
def get_Time():
    return {
        'Name':'Varun',
        'Age':'21',
        'Date': date,
        'HomeTown':'Bengaluru'
    }

