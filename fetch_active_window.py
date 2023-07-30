import subprocess


def get_active_window_title():
    try:
        script = 'tell application "System Events" to get name of (processes whose frontmost is true)'
        window_title = subprocess.check_output(['osascript', '-e', script]).decode().strip()
        return window_title
    except subprocess.CalledProcessError:
        return "Unknown"


if __name__ == "__main__":
    active_window_title = get_active_window_title()
    print("Active Window Title:", active_window_title)
