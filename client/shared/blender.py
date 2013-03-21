from subprocess import Popen
import subprocess
from time import sleep
import os

#os.setpgrp()




#


print "Launch blender!!!!"
#    cmd = "nice -n +10 /Applications/blender.app/Contents/MacOS/blender -b test.blend -o //files/job1_ -t 0 -F PNG -x 1 -f 21"
#    cmd = "/Applications/blender.app/Contents/MacOS/blender -b test.blend -o //files/job1_ -t 0 -F PNG -x 1 -f 21"
cmd = "/Applications/blender.app/Contents/MacOS/blender -b test.blend -o //files/job1_ -t 0 -F PNG -x 1 -s 1 -e 5 -a"
args = cmd.split()
#process = Popen(args)
subprocess.call(args)

"""
print "poll %s" % process.poll()
print "launch %s" % process

r = process.poll()
while (r == None):
    sleep(1)
    r = process.poll()
"""