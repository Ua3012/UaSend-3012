from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

data_file = 'users.json'

if not os.path.exists(data_file):
    with open(data_file, 'w') as f:
        json.dump({'users': []}, f)

def read_data():
    with open(data_file, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        data = read_data()
        data['users'].append({'name': username, 'msg': message})
        write_data(data)
        return redirect('/')
    data = read_data()
    return render_template('index.html', messages=data['users'])

if __name__ == '__main__':
    app.run(debug=True)
