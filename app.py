import fetch_active_window
import json
import time

data_path = "data/data.json"


def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def encode(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)


def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def is_json_file_empty(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            if not data:
                return True  # The JSON data is empty
            return False  # The JSON data is not empty
    except (FileNotFoundError, json.JSONDecodeError):
        return True


if is_json_file_empty(data_path):
    daily_dict = {}
else:
    daily_dict = load(data_path)

encode(daily_dict, data_path)

while True:
    daily_dict = load(data_path)
    active_window = fetch_active_window.get_active_window_title()
    if active_window not in daily_dict:
        print("NOT FOUND")
        daily_dict[active_window] = 0
    else:
        daily_dict[active_window] += 1

    print(active_window, seconds_to_hms(daily_dict[active_window]))
    encode(daily_dict, data_path)
    time.sleep(2)
