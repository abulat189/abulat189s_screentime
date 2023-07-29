import time
import json
from flask import Flask, render_template

app = Flask(__name__)

def load_process_data_from_json():
    try:
        with open('data.json', 'r') as json_file:
            process_data = json.load(json_file)
            return process_data
    except FileNotFoundError:
        return {}

def save_process_data_to_json(process_data):
    with open('data.json', 'w') as json_file:
        json.dump(process_data, json_file)

@app.route('/')
def index():
    process_data = load_process_data_from_json()
    return render_template('index.html', process_data=process_data)

if __name__ == '__main__':
    app.run(debug=True)
