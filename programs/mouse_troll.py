from pynput.mouse import *
import random
from time import sleep
import subprocess

subprocess.call("pip install pynput",shell=True)

mouse = Controller()

def randomMousePosition():
    random_x = random.randint(1,10000)
    random_y = random.randint(1,10000)
    moveMouse(random_x,random_y)

def moveMouse(x,y):
    mouse.move(x,y)
    print('[+] Mouse moved')

while True:
    randomMousePosition()
    sleep(1)
    mouse.click(Button.left,1)
    mouse.click(Button.right,1)