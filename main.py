from flask import Flask, request, redirect, escape
import html
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def is_empty(text):
    if not len(text) > 0:
        return True
    else:
        return False

@app.route('/validate', methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error =''
    verify_error = ''
    email_error = ''

@app.route('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route('/', methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)


app.run()
