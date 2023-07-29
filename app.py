import psutil
import time
from flask import Flask, render_template, jsonify
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

executor = ThreadPoolExecutor()

def get_process_data():
    process_data = {}
    for process in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            process_name = process.info['name']
            pid = process.info['pid']
            running_time = time.time() - process.info['create_time']

            process_data[process_name] = {
                'pid': pid,
                'running_time': running_time
            }

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return process_data

@app.route('/')
def index():
    # Get the process data asynchronously using a background thread
    future = executor.submit(get_process_data)
    process_data = future.result()

    return render_template('index.html', process_data=process_data)

@app.route('/api/process_data')
def api_process_data():
    # Get the process data asynchronously using a background thread
    future = executor.submit(get_process_data)
    process_data = future.result()

    return jsonify(process_data)

if __name__ == '__main__':
    # Run the Flask app using Gunicorn
    # The -w option specifies the number of worker processes
    # You can adjust the number of workers as needed
    # For example, -w 4 will run 4 worker processes
    app.run(host='0.0.0.0', port=5000, debug=False)
