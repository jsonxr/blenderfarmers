#!/usr/bin/env python
# Verified that this works on ubuntu
import commands

def battery_check():
    state = commands.getoutput("grep \"^charging state\" /proc/acpi/battery/BAT0/state | awk '{ print $3 }'")
    if state == "discharging":
        return True
    else:
        return False
 
if __name__ == "__main__": 
    if battery_check():
        print("battery")
    else:
        print("AC")