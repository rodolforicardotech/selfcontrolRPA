import os
import time
import pyautogui

#texto = "python -u selfcontrol.py"

os.system("open /Applications/SelfControl.app")

time.sleep(3)


pyautogui.click(1262, 298)

time.sleep(1)

pyautogui.typewrite("macbook")
pyautogui.hotkey("enter")
