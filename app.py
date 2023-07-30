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
    if active_window not in daily_dict:
        print("NOT FOUND")
        daily_dict[active_window] = 0
    else:
        daily_dict[active_window] += 1
    print(active_window, daily_dict[active_window])
    encode(daily_dict, "data.json")
    time.sleep(1)
