import os
p=os.getcwd()
args=[p+'/helloworld.py']
cpid=os.fork()
if cpid == 0:
    print('Child')
    os.execv('/usr/bin/python3',['python3']+args)
else:
    print('Parent')
    os.waitpid(0,0)
