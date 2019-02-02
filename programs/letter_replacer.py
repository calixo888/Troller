from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
import subprocess

subprocess.call("pip install pynput",shell=True)
# BE CAREFUL!!!!! AFTER RUNNING SCRIPT, IT WILL DELETE THE WHOLE CODE!!!!!!!

keyboard1 = Controller()
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def replace():
    fake_letter = random.choice(letters)
    keyboard1.press(fake_letter)

def on_release(key):
    counter = 0
    while counter == 0:
        keyboard1.press(Key.backspace)
        replace()
        counter += 1

def start():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

start()
exit()