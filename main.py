from tkinter import *
import keyboard as keyb
import pyautogui
import time
from keybind import KeyBinder

root = Tk()

def bind():
  start = bindStartBtn.get()        
  end = bindEndBtn.get()
  print(start, end)

  keyb.add_hotkey(start, lambda: startBot())

  iTrue = 0

  while iTrue == 0 :
    if keyb.is_pressed(end):
      print('Нажата клавиша выхода из программы')
      iTrue = 1
      exit(0)

def startBot():
  while(True):
    #Открывает меню, выбирает награды
    keyb.press_and_release("tab")
    pyautogui.moveTo(1200, 35, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    #Выбирает ежедневные награды
    pyautogui.moveTo(187, 107, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    #Забирает мульти кейс 
    pyautogui.moveTo(825, 325, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    #Забирает новогодний кейс
    # pyautogui.moveTo(1720, 325, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Закрывает меню
    keyb.press_and_release("tab")

    time.sleep(300) #Ждем 5 минут

#Окно проложения
root["bg"] = "#252525"
root.title("AutoCollector")
root.wm_attributes("-alpha", 1)
root.geometry("300x300")

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=300)
canvas.pack()

frame = Frame(root, bg="#252525")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

startBotBtn = Button(frame, text="Start bot", bg="green", font=40, command=bind)
startBotBtn.pack()

bindStartBtn = Entry(frame, bg="white")
bindStartBtn.pack()

bindEndBtn = Entry(frame, bg="white")
bindEndBtn.pack()

root.mainloop()
