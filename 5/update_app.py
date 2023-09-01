import subprocess
import sys

import pandas as pd
import psutil


def main():
    # get the app name from command lien argument
    if len(sys.argv) != 2:
        sys.exit("Usage: update_app.py <app_name>")
    app_name = str.strip(sys.argv[1])

    # get all the processes
    processes = get_processes()

    # the the pid of the process
    app_process = processes[processes["name"] == app_name].index

    # kill process
    for pid in app_process:
        process = psutil.Process(pid=pid)
        process.kill()

    # update the app that is installed with snapstore
    subprocess.run(["sudo", "snap", "refresh", app_name])


# all processes
def get_processes() -> pd.DataFrame:
    return pd.DataFrame(
        data={p.pid: p.info for p in psutil.process_iter(["username", "name"])}
    ).transpose()


if __name__ == "__main__":
    main()
