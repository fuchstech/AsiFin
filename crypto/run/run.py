
import os

def run(command):
    print(os.popen('ls').read())
run("aa")