import pyautogui
import time
time.sleep(5)
file = open("/home/kali/Documents/Pyautugui/words",'r')
for word in file:
	pyautogui.typewrite(word)


	
	pyautogui.press("enter")




