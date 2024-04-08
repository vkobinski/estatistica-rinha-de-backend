import re
from openpyxl import Workbook

log_file = "./simulation.log"

fields = {}
lines = []


with open(log_file, "r") as file:
    for line in file:
        match = line.startswith("REQUEST")
        if match:
            parts = line.strip().split()
            operation = parts[1]
            start_time = parts[2]
            end_time = parts[3]
            total_time = int(end_time) - int(start_time)
            time_since_start = 0
            if len(lines) > 0:
                time_since_start = int(start_time) - int(lines[0][1])

            add_start_time = start_time[0:10]

            lines.append((operation, start_time, total_time,time_since_start))
            if fields.get(add_start_time) is None:
                fields[add_start_time] = 1
            else:
                fields[add_start_time] = fields[add_start_time] + 1


# Writing to Excel
wb = Workbook()
ws = wb.active
ws.append(["Operation", "Start Time", "Total Time (ms)", "Time Since Start (ms)", "Simultaneous Requests"])

for (operation, start_time, total_time, time_since_start) in lines:
    simul = fields.get(start_time[0:10])
    if simul is None:
        simul = 1
    ws.append([operation, start_time, total_time, time_since_start,simul])

excel_file = "./simulation_data.xlsx"
wb.save(excel_file)

print(f"Data has been written to {excel_file}")