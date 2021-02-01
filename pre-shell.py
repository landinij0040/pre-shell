import os
import sys

if __name__ == "__main__":
    n = os.fork()
    # n greater than 0 means parent process
    if n > 0:
        print("Parent process and id is : ", os.getpid())
    # n equals to 0 means child process
    else:
        print("Child process is : ", os.getpid())
        os.execv('/usr/bin/python3', ['python3'] + [os.getcwd()+'/helloworld.py'])
