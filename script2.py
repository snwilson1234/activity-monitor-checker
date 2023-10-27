import psutil
from humanize import naturalsize
import os

mem = psutil.virtual_memory()

swap_mem = psutil.swap_memory()

available_mem = naturalsize(mem.available, binary=True)

print("available: " + available_mem)

available_mem = available_mem.split(' ')[0]

if float(available_mem) <= 5:#validate mem usage. if too high trigger activity monitor. can change val as needed.
    path = "/System/Applications/Utilities/Activity\ Monitor.app"
    os.system(f"open {path}")