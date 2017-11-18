from flask import Flask, request, redirect
import html


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Signup</title>
    </head>
    <body>
        <h1>Signup</h1>
"""
# add signup form
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
       <table>
        <tbody>
        <tr>
            <td>
                <label for="username">Username</label>
            </td>
            <td>
                <input name="username" value="" type="text">
                <span class="error"> That's not a valid username</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for="password">Password</label>
            </td>
            <td>
                <input name="password" type="password">
                <span class="error">That's not a valid password</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for="verify">Verify Password</label>
            </td>
            <td>
                <input name="verify" type="password">
                <span class="error"> Passwords don't match</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for="email">Email (optional)</label>
            </td>
            <td>
                <input name="email" value="">
                <span class="error"></span>
            </td>
        </tr>
       </tbody>
       </table>
        <input type="submit" value="Sign in">
      </form>
    </body>
</html
"""

page_footer = """
    </body>
</html>
"""
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

@app.route("/")
def index():
    return form

@app.route('/hello', methods=['POST'])
def hello():
    username =  request.form['username']
    return '<h1>Hello, ' + html.escape(username) + '!' + '</h1>'

app.run()
