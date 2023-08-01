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
    usage_times_ = load(data_path)
    table = self.query_one(DataTable)
    for app in usage_times_:
        table.update_cell(app, "1", app)
        table.update_cell(app, "2", seconds_to_hms(usage_times[app]))
        table.add_row("1", "2")


class ScreenTimes(App):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header(name="abulat189s_screentime", show_clock=True)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_column("Application", key="1")
        table.add_column("Time", key="2")
        table.add_row("1", "2", key="3")
        _usage_times = load(data_path)
        for app_ in _usage_times:
            table.add_row(app_, seconds_to_hms(_usage_times[app_]), key=app_)
        self.set_interval(3, update_table(self), repeat=0)

    def on_button_pressed(self) -> None:
        self.exit()


# Your dictionary of usage times
usage_times = load(data_path)

if __name__ == "__main__":
    app = ScreenTimes()
    app.run()
