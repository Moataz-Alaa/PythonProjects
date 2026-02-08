
# Program to execute a sequence of keyboard inputs on loop

# PLEASE DON'T EDIT THIS FILE DIRECTLY TAKE A COPY AND EDIT YOUR OWN COPY
# KEEP THE ORIGNAL WORKING CODE AS IT IS


from pynput.keyboard import Key, Controller, Listener
import time
import threading

start_stop_key = Key.f2     # Key to start and stop the program, it will start stopped unless the wait_before_start option is enabled
quit_key = 'q'              # Key to exit the program, must be a lower case character (so the case ignore works) 
                            # or you can change the implementation to make it something else
resume_wait_time = 3        # Time before resuming after pressing the start_stop_key (seconds)
wait_before_start = False   # Option to wait a custom time before first run
                            # WARNING: the program will start IMMEDIATELY after the countdown if this option is enabled
start_wait_time = 10        # Time to wait before starting the first run if wait_before_start is enabled



keyboard = Controller()

stop_flag = True   # Used to stop and resume the sequence
exit_flag = False  # Used to quit the program completely

def recorded_sequence():
    # Placeholder for your sequence logic
    # Example (remove when you define your own):
    keyboard.press(Key.right)
    time.sleep(0.05)  # Hold for 50 ms
    keyboard.release(Key.right)
    time.sleep(0.2)   # Wait before next press

# def recorded_sequence():
#     # Placeholder for your sequence logic
#     # Example (remove when you define your own):
#     keyboard.tap('a')
#     time.sleep(0.12)
#     keyboard.tap('b')
#     time.sleep(0.12)
#     keyboard.tap('c')
#     time.sleep(0.12)
#     keyboard.tap('d')
#     time.sleep(1)     # Never forget to add a longer wait before starting the next loop
#     keyboard.tap(Key.space)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Started sequence.")

def play_sequence_on_loop():
    global stop_flag, exit_flag
    while not exit_flag:
        if not stop_flag:
            recorded_sequence()
        else:
            time.sleep(0.05)  # Avoid high CPU usage when stopped

def on_press(key):
    global stop_flag, exit_flag

    try:
        if key == start_stop_key:  # Start sequence
            if stop_flag:          # Run 3-second countdown on resume
                print("Starting in...")
                countdown(resume_wait_time)
                stop_flag = False
            else:
                stop_flag = True
                print("Stopped sequence.")

        elif key.char and key.char.lower() == quit_key:  # Quit program
            stop_flag = True
            exit_flag = True
            print("Exiting program...")
            return False  # Stop listener

    except AttributeError:
        pass

if wait_before_start:      
    print("Starting in...")
    countdown(start_wait_time)
    stop_flag = False

# Start pressing thread
threading.Thread(target=play_sequence_on_loop, daemon=True).start()

# Start listener
with Listener(on_press=on_press) as listener:
    listener.join()

print("Program ended.")
