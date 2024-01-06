import keyboard
import pyautogui
import time

def auto_clicker(delay, button):
    while True:
        time.sleep(delay)
        pyautogui.click(button=button)
        if keyboard.is_pressed('Esc'):
            break

auto_clicker(0.1, 'left')