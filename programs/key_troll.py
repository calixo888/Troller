from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
from time import sleep
import subprocess

subprocess.call("pip install pynput",shell=True)
keyboard = Controller()
creepy_phrases = {1:"I'm watching you :)",2:"I know what you're typing :)",3:"I have hacked your computer :)",4:"You are not safe :)",5:"Watch your back :)"}

def on_release():
    random_phrase = random.randint(1,5)
    for i in creepy_phrases[random_phrase]:
        keyboard.press(i)
        keyboard.release(i)

while True:
    sleep(2)
    on_release()