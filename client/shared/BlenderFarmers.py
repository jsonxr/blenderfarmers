#!/usr/bin/env python

import argparse
import time
import datetime
import sys

import application

print "BlenderFarmers Starting..."

parser = argparse.ArgumentParser(description='Runs a command after the computer has been idle for a period of time.')
parser.add_argument('-b','--background', action="store_true", help='This launches the application in the background to communicate with the server.  If this argument is not supplied, then all parameters are ignored and the GUI application is launched.')
args = parser.parse_args()



#if (args.background):
while True:
    now = datetime.datetime.now()
    print str(now)
    sys.stdout.flush()
    time.sleep(1)
#else:
#    app = application.Application()
#    app.MainLoop()
