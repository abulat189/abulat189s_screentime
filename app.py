import fetch_active_window
import json
import time


def encode(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)


def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


daily_dict = {}
encode(daily_dict, "data.json")

while True:
    daily_dict = load("data.json")
    active_window = fetch_active_window.get_active_window_title()
    print(active_window)
    time.sleep(1)
