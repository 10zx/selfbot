from pynput.keyboard import Key, Controller
import time

# Establish Keyboard
keyboard = Controller()

# Time to click client
time.sleep(10)

# Main Loop
while True:
    # Key in !d bump
    keyboard.press('!')
    keyboard.release('!')
    keyboard.press('d')
    keyboard.release('d')
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    keyboard.press('b')
    keyboard.release('b')
    keyboard.press('u')
    keyboard.release('u')
    keyboard.press('m')
    keyboard.release('m')
    keyboard.press('p')
    keyboard.release('p')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    print('server !d bumped')
    
    # Sleep
    for i in range(7210, 0, -1):
        time.sleep(1)
        print(f'sleeping for {i} more seconds')




