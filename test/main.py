import customtkinter
import json
import keyboard as keyb
import pyautogui

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
status = "Готов к запуску!"

#MAIN GUI
root.geometry("300x100")
root.attributes("-topmost", True)
root.title("AutoCollector")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

statusBar = customtkinter.CTkLabel(master=frame, text="Готов к запуску!")

startBtn = customtkinter.CTkButton(master=frame, text="Start", width=10, command= lambda: hotKey())
startBtn.pack(pady=0, padx=0)
startBtn.place(x=180, y=40)

settingBtn = customtkinter.CTkButton(master=frame, text="Settings", width=10, command=lambda: settingsGui())
settingBtn.pack(pady=0, padx=0)
settingBtn.place(x=110, y=40)

statusBar.pack(pady=0, padx=0)

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

def getSettings():
  with open("config.json", "r") as file:
    data = file.read()
    jsonData = json.loads(data)

  return jsonData

def hotKey():
  keyb.add_hotkey(getSettings().get("bindStartButton"), lambda: startBot())

  i = 0
  while(i == 0):
    if keyb.is_pressed(getSettings().get("bindEndButton")):
      print("Stop button was clicked")
      i = 1
      exit(0)

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

#BOT
def startBot():
  print("bot start")
  while(True):
    #Открывает меню, выбирает награды
    # statusBar(text="Открываю меню")
    # keyb.press_and_release("tab")
    # headGui.changeText("Выбираю \"награды\"")
    pyautogui.moveTo(1200, 35, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Выбирает ежедневные награды
    # state="Выбираю \"Ежедневные награды\""
    pyautogui.moveTo(187, 107, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Забирает мульти кейс
    # state="Забираю мульти кейс"
    pyautogui.moveTo(825, 325, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Забирает новогодний кейс, если указал пользователь
    if Utils.getSettings().get("isSecondBox"):
      # state="Забираю новогодний кейс"
      pyautogui.moveTo(1720, 325, duration=1)
      # pyautogui.click(clicks=1, interval=0.5)

    #Закрывает меню
    # state="Закрываю меню"
    # keyb.press_and_release("tab")
  
    # state="Жду 5 минут до следующего цикла"
    time.sleep(2) #Ждем 5 минут


root.mainloop()