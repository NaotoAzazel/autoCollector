import customtkinter
import json
import keyboard as keyb
import pyautogui
import time
import tkinter as tk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

state = {0: "Готов к запуску!", 1: "Открываю меню", 2: "Выбираю \"награды\"", 3: "Выбираю \"Ежедневные награды\"", 4: "Забираю мульти кейс", 5: "Закрываю меню", 6: "Жду 5 минут до следующего цикла", 7: "Забираю новогодний кейс"}

counter = 0
saveBack = 0

running = False

def getSettings():
  with open("config.json", "r") as file:
    data = file.read()
    jsonData = json.loads(data)

  return jsonData

def stop():
  global running
  running = False

def stopBot():
  global running
  keyb.add_hotkey(getSettings().get("bindEndButton"), stop)
  root.after(200, stopBot)

#BOT
def startBot():
  global counter, saveBack, running
  running = True

  if running:
    while(True):
      #Открывает меню, выбирает награды
      counter += 1
      # keyb.press_and_release("tab")
      counter += 1
      pyautogui.moveTo(1200, 35, duration=1)
      # pyautogui.click(clicks=1, interval=0.5)

      #Выбирает ежедневные награды
      counter += 1
      pyautogui.moveTo(187, 107, duration=1)
      # pyautogui.click(clicks=1, interval=0.5)

      #Забирает мульти кейс
      counter += 1
      pyautogui.moveTo(825, 325, duration=1)
      # pyautogui.click(clicks=1, interval=0.5)

      saveBack = counter

      #Забирает новогодний кейс, если указал пользователь
      if getSettings().get("isSecondBox"):
        # state="Забираю новогодний кейс"
        pyautogui.moveTo(1720, 325, duration=1)
        counter = 7
        # pyautogui.click(clicks=1, interval=0.5)

      counter = saveBack

      #Закрывает меню
      # state="Закрываю меню"
      counter += 1
      # keyb.press_and_release("tab")

      # state="Жду 5 минут до следующего цикла"
      counter += 1
      time.sleep(2) #Ждем 5 минут
      counter = 0

def changeText():
  statusBar.configure(text=state[counter])
  root.after(1000, changeText)

#UTILS
def applyChanges(window, startBtn, endBtn, isSecondBox):
  with open("config.json", "w") as file:
    json.dump(
      {
        "isSecondBox": isSecondBox,
        "bindStartButton": startBtn,
        "bindEndButton": endBtn
      },
      file
    )
  window.destroy()

#SETTINGS GUI
def settingsGui():
  window = customtkinter.CTkToplevel(root)

  window.geometry("400x270")
  window.title("Settings")

  frame = customtkinter.CTkFrame(master=window)
  frame.pack(pady=20, padx=60, fill="both", expand=True)

  label = customtkinter.CTkLabel(master=frame, text="Кнопка для запуска").pack()

  bindStartBtn = customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для запуска")
  bindStartBtn.pack(padx=12, pady=10)
  bindStartBtn.insert(0, getSettings().get("bindStartButton"))

  label2 = customtkinter.CTkLabel(master=frame, text="Кнопка для завершения").pack()

  bindEndBtn= customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для завершения")
  bindEndBtn.insert(0, getSettings().get("bindEndButton"))
  bindEndBtn.pack(padx=12, pady=10)

  index = customtkinter.BooleanVar(value=getSettings().get("isSecondBox"))
  isSecondBox = customtkinter.CTkCheckBox(master=frame, text="Забирать новогодний кейс", variable=index, onvalue=True, offvalue=False).pack()

  applyBtn = customtkinter.CTkButton(master=frame, text="Сохранить изменения", command=lambda: applyChanges(window, bindStartBtn.get(), bindEndBtn.get(), index.get()))
  applyBtn.pack(padx=12, pady=10)

  window.mainloop()

#MAIN GUI
root = customtkinter.CTk()

root.geometry("300x100")
root.attributes("-topmost", True)
root.title("AutoCollector")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

statusBar = customtkinter.CTkLabel(master=frame, text="Status")
statusBar.pack(pady=0, padx=0)

startBtn = customtkinter.CTkButton(master=frame, text="Start", width=10, command= lambda: keyb.add_hotkey(getSettings().get("bindStartButton"), startBot))
startBtn.pack(pady=0, padx=0)
startBtn.place(x=180, y=40)

settingBtn = customtkinter.CTkButton(master=frame, text="Settings", width=10, command=settingsGui)
settingBtn.pack(pady=0, padx=0)
settingBtn.place(x=110, y=40)


stopBot()
changeText()
root.mainloop()