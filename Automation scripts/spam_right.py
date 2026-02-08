from pynput.keyboard import Key, Controller, Listener
import time
import threading

keyboard = Controller()
stop_flag = False           # Stop when True

def press_right_arrow():
    # global stop_flag      # Doesn't need this line because this function only reads the global variable stop_flag
    # If you create a stop_flag variable in this scope it would be a new local variable unrelated to the global stop_flag
    
    # 10-second countdown before starting
    # Time used for switching to the window where the script is needed
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("Started.")
    
    while not stop_flag:
        # Using keyboard.tap(Key.right) (keyboard.press(Key.right) + keyboard.release(Key.right))
        # is not recommended, tried it for a game and didn't work as expected
        keyboard.press(Key.right)
        time.sleep(0.05)             # Hold for 50 miliseconds then release
        keyboard.release(Key.right) 
        time.sleep(0.2)              # 200 miliseconds between taps

def on_press(key):
    global stop_flag        # Must insert this line to write in the stop_flag variable outside the function
    # You can't create a new stop_flag variable here, assignment will only overwrite the global one

    try:
        if key.char and key.char.lower() == 'q':  # Stop when 'q' is pressed and ignore case
            # key.char --> True if the pressed key is a character
            # key.char.lower() == 'q' --> If the pressed key is a character,
            # take its lower case and compare it to 'q' (useful when Caps Lock is on) 
            stop_flag = True
            return False  # stop listener
    except AttributeError:
        pass

# Start pressing in a separate thread
threading.Thread(target=press_right_arrow, daemon=True).start()

# Listen for 'q' or 'Q'
with Listener(on_press=on_press) as listener:
    listener.join()

# One thread presses the button and the other (main thread) listens for the stop key press

print("Stopped.")
