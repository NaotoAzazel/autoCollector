import tkinter as tk
import pyautogui
import time
import keyboard as keyb

status = {0: "Открываю меню", 1: "Захожу в награды", 2: "Забираю мульти кейс"}

i = 0
def bot():
	global i
	while(True):
		pyautogui.moveTo(1200, 35, duration=1)
		i += 1
		pyautogui.moveTo(1100, 35, duration=1)
		i += 1
		time.sleep(3)
		i = 0

keyb.add_hotkey("M", bot)


def setLabel():
	print(status[i])
	label["text"] = status[i]
	root.after(1000, setLabel)

root = tk.Tk()
root.geometry("500x300")
label = tk.Label(root, text="placeholder")
label.pack()

setLabel()
root.mainloop()