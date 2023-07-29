from flask import Flask, render_template
import json


def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


app = Flask(__name__)
process_data = load("data.json")


@app.route('/')
def index():
    return render_template('index.html', process_data=process_data)


if __name__ == '__main__':
    app.run(debug=True)
