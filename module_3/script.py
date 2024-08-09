#!/usr/bin/env python3

import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_cpu_usage() or not check_disk_usage("/") :
    print("Computer is not healthy")
else:
    print("Every thing is Ok healthy!!!!!!!!!! ")    
    
    
# this script is for checking health of computer by free space should be greater than 20% or cpu usage is less than 75%  


