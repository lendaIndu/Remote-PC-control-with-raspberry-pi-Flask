from flask import Flask

from flask import Flask, flash, redirect, render_template, request, session, abort

import os

import hashlib

state = 'off'

app = Flask(__name__)


def pc_action(move):
    if move == 'turn_on':
        os.system('python /make_your_own_directory/turn_on_pc.py')


@app.route('/')
def index():
    if not session.get('logged_in'):

        return render_template('login.html')

    else:

        response = os.system('ping -c 1 192.168.0.000')  # input your PC IP address

        if response == 0:

            pingstatus = "Active"

        else:

            pingstatus = "Down"

        state = pingstatus

        return render_template('index.html', state=state)


@app.route('/move/<move>')
def pc_move(move):
    if not session.get('logged_in'):

        return render_template('login.html')

    else:

        global state

        state = move

        pc_action(state)

        print('PC %s' % state)

        state = "ON"

        return render_template('main.html', state=state)


@app.route('/move/main')
def main():
    if not session.get('logged_in'):

        return render_template('login.html')

    else:

        response = os.system('ping -c 1 192.168.0.000')  # input your PC IP address

        if response == 0:

            pingstatus = "Active"

        else:

            pingstatus = "Down"

        state = pingstatus

        return render_template('index.html', state=state)


@app.route('/login', methods=['POST'])
def do_admin_login():
    if hashlib.sha1(request.form['password']).hexdigest() == 'make_your_own_hash':  # turn your password to hash

        session['logged_in'] = True

        return render_template('index.html', state=state)



    else:

        flash('wrong password!')

        return render_template('login.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)

    app.run(debug=False, host='0.0.0.0', port=12345)
