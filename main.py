from flask import Flask,render_template,jsonify
import pandas as pd

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    data = pd.read_csv('data.csv')

    # Convert the timestamp column to datetime format
    data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], format='%d/%b/%Y:%H:%M:%S:%z')

    # Extract the date and hour from the timestamp
    data['Date'] = data['TIMESTAMP'].dt.date
    data['Hour'] = data['TIMESTAMP'].dt.strftime('%H:%M:%S')

    # Count the occurrences of each date
    date_counts = data['Date'].value_counts().sort_index()

    # Prepare the original data for Highcharts
    original_data = [{'name': str(date), 'y': count} for date, count in date_counts.items()]

    # Group the data by date and hour, and calculate the hourly counts
    hourly_data = data.groupby(['Date', 'Hour']).size().reset_index(name='Count')

    # Prepare the hourly data for Highcharts
    hourly_data_dict = {}
    for _, row in hourly_data.iterrows():
        date = str(row['Date'])
        hour = row['Hour']
        count = row['Count']
        if date not in hourly_data_dict:
            hourly_data_dict[date] = []
        hourly_data_dict[date].append([hour, count])

    return render_template('dashboard.html',original_data=original_data, hourly_data=hourly_data_dict)

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