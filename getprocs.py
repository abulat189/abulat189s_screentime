import psutil
import time
import json

file_path = "data.json"
def encode(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

while True:
    process_data = {}# = load("data.json")
    for process in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            process_name = process.info['name']
            pid = process.info['pid']
            running_time = time.time() - process.info['create_time']

            process_data[process_name] = {
                'pid': pid,
                'running_time': running_time
            }
            running = time.time() - process.info['create_time']
            print(
                f'Process {process.name()} with PID {process.pid}  {running:.2f} seconds')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    encode(process_data, "data.json")
    print("Dictionary saved to JSON file successfully.")
    time.sleep(10)

    encode(process_data, "data.json")





