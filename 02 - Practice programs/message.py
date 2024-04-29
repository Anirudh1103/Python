import pyautogui
import time
time.sleep(5)
count = 0
while count <=100:
    pyautogui.typewrite("I LOVE YOU THE MOST MINION <3")
    pyautogui.press('enter')
    count = count +1
    