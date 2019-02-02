import webbrowser
from time import sleep
import subprocess

subprocess.call("pip install webbrowser",shell=True)
subprocess.call("pip install pynput",shell=True)
while True:
    webbrowser.open([RANDOM URL])
    sleep(2)