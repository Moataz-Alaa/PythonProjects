from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(10)

keyboard.press(Key.shift)
keyboard.press('a')
keyboard.release(Key.shift)
keyboard.release('a')
