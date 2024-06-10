# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {'user1': 'password1'}

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome {session['username']}! <br> <a href='/logout'>Logout</a>"
    return "Welcome to the Home Page <br> <a href='/login'>Login</a> - Updated"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username:
            flash('Username is required')
            return redirect(url_for('login'))
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
