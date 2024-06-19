import keyboard
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Is off')
    else:
        isClicking = True
        print('Is on')


keyboard.add_hotkey('alt+x', set_clicker)

try:
    while True:
        if isClicking:
            mouse.double_click(button='left')
            time.sleep(0.02)                          # Интервал между двойными кликами
except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    print("Program terminated")
