import os

os.execv('/usr/bin/cat', ['cat', '/proc/cpuinfo'])
