import psutil
def sec2hours(secs):
    mm, ss = divmod (secs,60)
    hh, mm = divmod (mm,60)
    return "%d:%02d:%02d" % (hh, mm , ss)
print ("CPU Percentage:")
print (psutil.cpu_percent(interval=1),"\n")
print ("Virtual Memory:")
print (dict(psutil.virtual_memory()._asdict()),"\n")
print ("Disk Partitions:")
print(psutil.disk_partitions(),"\n")
battery = psutil.sensors_battery()
print ("Battery info:")
print ("charge = %s%%, time left = %s" % (battery.percent,sec2hours(battery.secsleft)))
