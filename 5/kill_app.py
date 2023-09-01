import sys

import pandas as pd
import psutil


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: update_app.py <app_name>")

    app_name = str.strip(sys.argv[1])

    processes = get_processes()
    app_process = processes[processes["name"] == app_name].index

    # kill process
    for pid in app_process:
        process = psutil.Process(pid=pid)
        process.kill()


# all processes
def get_processes() -> pd.DataFrame:
    return pd.DataFrame(
        data={p.pid: p.info for p in psutil.process_iter(["username", "name"])}
    ).transpose()


if __name__ == "__main__":
    main()
