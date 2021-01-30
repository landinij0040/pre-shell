# print("Files in %r: %s" % (cwd, files))
import sys
import os
if __name__ == '__main__':
    # cwd = os.getcwd() # Get the current working directory
    # files = os.listdir(cwd)

    print("This is the name of the other script: ", sys.argv[1])


    os.execv('helloworld.py',sys.argv [1:])
