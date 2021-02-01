import os
import sys
if __name__ == "__main__":
    path = ['/usr/bin/cat', '/usr/bin/echo', '/usr/bin/python3', '/usr/bin/uname']
    args = [['cat', '/proc/cpuinfo'],['echo','Hello World'],['python3', 'spinner.py',' 1000000'],['uname', '-a']]
    for i in range(len(path)):
        n = os.fork()
        if n > 0: # n greater than 0 means parent process
            the_wait_value = os.waitpid(n,0)
        else: # n equals to 0 means child process
            os.execv(path[i], args[i] )
    n = os.fork()
    if n > 0: # Parent process
        exit()
    else: #child process
        os.execv('/usr/bin/python3', ['python3','spinner.py','2000000',])
