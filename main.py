from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def empty(str):
    if str == []:
        return True

@app.route("/signup", methods=['POST'])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if empty(username):
        username_error = 'Username name not valid'
        username = ''
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = 'Username out of range (3-20 characters)'
            username = ''

    if empty(password):
        password_error = 'Enter password'
        password = ''
    else:
        if len(password) < 3 or len(password) >20:
            password_error = 'Password out of range (3-20 characters)'
            password = ''
    
    if verify_password != password:
        verify_error = 'Password Should match!'
        verify_password = ''

    if email:
        if email.count("@") < 1 or email.count("@") > 1:
            email_error = 'Must enter valid email!'
        if email.count(".") < 1 or email.count(".") > 1:
            email_error = 'Must enter valid email!'
        if " " in email:
            email_error = "Must enter valid email!"
        if len(email) < 3 or len(email) > 20:
            email_error = "Email length out of range(3-20)"

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user-signup.html',username_error=username_error,
        password_error=password_error, verify_error=verify_error,
        email_error=email_error, username=username,email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', user=username)                                
@app.route("/")
def index():
    return render_template('user-signup.html')


app.run()