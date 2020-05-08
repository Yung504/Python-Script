import psutil
import os
import shutil
import socket
import platform
from requests import get

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_sysinfo():
    d=dict()
    uname = platform.uname()

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"

    d["Battery1"]=(percent+'% | '+plugged)
    d["CPU"]=uname.processor

    p = psutil.Process(os.getpid())
    d["CPU Usage:"]=p.cpu_percent()

    total, used, free = shutil.disk_usage("/")
    d["Disk (/)"]= (used // (2**30))/(total // (2**30))*100

    d["GPU"]=uname.processor
    d["GPU Driver"]=uname.machine

    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    d["Host"]=host_name
    d["Kernel"]=uname.version
    d["Local IP "]=host_ip

    svmem = psutil.virtual_memory()
    d["Memory"]=get_size(svmem.available)

    d["OS"]=uname.system
    d["Public IP"] = get('https://api.ipify.org').text
    d["Uptime"] = psutil.boot_time()
    d["Users"]=uname.node
    return d


