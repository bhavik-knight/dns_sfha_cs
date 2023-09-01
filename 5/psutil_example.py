import pandas as pd
import psutil

processes_data = {p.pid: p.info for p in psutil.process_iter(["name", "username"])}
processes = pd.DataFrame(data=processes_data).transpose()
print(processes)
