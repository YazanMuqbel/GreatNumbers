from flask import Flask, render_template, request, redirect, session;
import random

app= Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1,100)

    if 'guess' not in session:
        session['guess']=0
    
    print(session['random'])
    print(session['guess'])
    return render_template('index.html', random=session['random'], guess=session['guess'])

@app.route('/process', methods=['POST'])
def process():
    session['guess']=int(request.form['guess'])
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect ('/')

if __name__== '__main__':
    app.run(debug=True)