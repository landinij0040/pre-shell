import os

if __name__ == "__main__":
    n = os.fork()

    # n greater than 0 means parent process
    if n > 0:
        print("Parent process and id is : ", os.getpid())
    
    # n equals to 0 means child process
    else:
        print("Child process and is is : ", os.getpid())
    
