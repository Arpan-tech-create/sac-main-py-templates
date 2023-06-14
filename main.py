from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/billing')
def bil():
    return render_template('billing.html')

@app.route('/icons')
def ic():
    return render_template('icons.html')

@app.route('/map')
def map1():
    return render_template('map.html')

@app.route('/notifications')
def noti():
    return render_template('notifications.html')

@app.route('/profile')
def pro():
    return render_template('profile.html')

@app.route('/rtl')
def rt():
    return render_template('rtl.html')

@app.route('/sign-in')
def insign():
    return render_template('sign-in.html')

@app.route('/sign-up')
def outsign():
    return render_template('sign-up.html')

@app.route('/tables')
def tab():
    return render_template('tables.html')

@app.route('/virtual-reality')
def vir():
    return render_template('virtual-reality.html')

@app.route('/typography')
def ty():
    return render_template('typography.html')


app.run(debug=True,port=5006)