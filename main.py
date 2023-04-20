from flask import Flask, render_template, request
import datetime
import smtplib
import os, random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


def error():
    return render_template('ErrorPage.html')

@app.route('/activities')
def activities():
    return error()
@app.route('/home')
def home():
    return error()
@app.route('/articles')
def articles():
    return error()
@app.route('/about-us')
def about_us():
    return error()
@app.route('/FAQs')
def faqs():
    return error()






if __name__ == '__main__':
    app.run(debug=True)