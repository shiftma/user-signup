from flask import Flask, request, redirect, render_template
import html
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

    
@app.route('/')
def index():
    return render_template('index.html')

def is_empty(text):
    if not len(text) > 0:
        return True
    else:
        return False

def valid_length(text):
    if len(text) < 3 or len(text) > 20:
        return False
    else:
        return True

@app.route('/', methods=['POST'])
def validate():

    username = str(request.form['username'])
    password = str(request.form['password'])
    verify = str(request.form['verify'])
    email = str(request.form['email'])

    username_error = ''
    password_error =''
    verify_error = ''
    email_error = ''

#Username validation
    if is_empty(username) or not valid_length(username):
        username_error = 'That\'s not a valid username'
#Password validation   
    if is_empty(password) or not valid_length(password):
        password_error = 'That\'s not a valid password'
#Verify password validation
    if is_empty(verify) or password != verify:
        verify_error = 'Passwords don\'t match'

#Email REGEX validation
    email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    def valid_email(mail):
        return email_re.match(email)

    if email:
        if not valid_email(email): 
            email_error = 'Email is not valid'   
        elif not valid_length(email):
            email_error = 'Email length must be more than 3 and less than 20 characters' 

    # if no error occurred return welcome page, else return error message
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', user_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)


app.run()
