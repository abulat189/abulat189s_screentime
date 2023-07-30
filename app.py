from flask import Flask, jsonify
import time
import json

app = Flask(__name__)
data_path = "data/data.json"

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


# Your dictionary of usage times
usage_times = load(data_path)

