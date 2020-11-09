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

if __name__ == '__main__':
    app.run(debug=True)
