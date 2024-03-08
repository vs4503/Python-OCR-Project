from flask import Flask
import datetime

date = datetime.datetime.now()

app = Flask(__name__)

@app.route('/data')
def get_Time():
    return {
        'Name':'Vikrant',
        'Age':'18',
        'Date': date,
        'HomeTown':'New Delhi'
    }

