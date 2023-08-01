from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header
from textual import events
import time
import json

data_path = "data/data.json"


def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def load(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def update_table(self):
    usage_times = load(data_path)
    table = self.query_one(DataTable)
    table.clear()
    time.sleep(3)
    for app in usage_times:
        table.add_row(app, seconds_to_hms(usage_times[app]), key=app)


class screentimes(App):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header(name="abulat189s_screentime", show_clock=True)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Application", "Time")
        usage_times = load(data_path)
        for app in usage_times:
            table.add_row(app, seconds_to_hms(usage_times[app]), key=app)

    def set_interval(self, interval=2):
        update_table()

    def on_button_pressed(self) -> None:
        self.exit()


# Your dictionary of usage times
usage_times = load(data_path)

if __name__ == "__main__":
    app = screentimes()
    app.run()
