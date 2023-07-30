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


@app.route('/')
def index():
    return """
    <html>
        <head>
            <script>
                function updateData() {
                    fetch('/data')
                    .then(response => response.json())
                    .then(data => {
                        // Update the HTML table with the 'data' received from the server
                        const tableBody = document.getElementById('tableBody');
                        tableBody.innerHTML = '';

                        for (const [app, time] of Object.entries(data)) {
                            const row = tableBody.insertRow();
                            const cell1 = row.insertCell();
                            const cell2 = row.insertCell();
                            cell1.innerHTML = app;
                            cell2.innerHTML = time;
                        }
                    });
                }
                setInterval(updateData, 5000); // Update every 5 seconds
            </script>
        </head>
        <body>
            <h1>Usage Times:</h1>
            <table>
                <thead>
                    <tr>
                        <th>Application</th>
                        <th>Usage Time</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                </tbody>
            </table>
        </body>
    </html>
    """


@app.route('/data')
def get_data():
    # Simulate data update with the current timestamp
    usage_times = load(data_path)
    for app in usage_times:
        usage_times[app] = int(time.time())

    return jsonify(usage_times)


if __name__ == '__main__':
    app.run(debug=True)
