import shutil
import psutil

diskUsage = shutil.disk_usage("/")

print(diskUsage)
# usage(total=175551815680, used=81078534144, free=85481168896)

print( diskUsage.free / diskUsage.total * 100 )
# 48.69198375242917  is perscentage of free disk space 

print(psutil.cpu_percent(5))
# this is a usage of cpu its is average time start of time and end of time that given as arrgument in seconds
