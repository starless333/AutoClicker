import threading
import time
import keyboard
from pynput.mouse import Button, Controller
delay = 0.01
button = Button.left
mouse = Controller()

try:
    while True:
        keyboard.wait('esc')
        while True:
            if keyboard.is_pressed('q'):
                break
            mouse.click(button)
            time.sleep(delay)
except KeyboardInterrupt as e:
    print(e)