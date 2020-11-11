from flask import Flask, render_template,request,redirect,url_for,session
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Login')

@app.route('/form.html')
def form():
    return render_template('form.html', the_title='New Form')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html', the_title='Dashboard')

@app.route('/supplier')
def runform():
    return render_template('supplier.html')

@app.route('/output')
def runform():
    return render_template('output.html')

@app.route('/process')
def runform():
    return render_template('process.html')

@app.route('/input')
def runform():
    return render_template('input.html')

@app.route('/customer')
def runform():
    return render_template('customer.html')

@app.route('/newjob')
def runform():
    return render_template('newjob.html')

@app.route('/complete')
def runform():
    return render_template('complete.html')

if __name__ == '__main__':
    app.run(debug=True)
