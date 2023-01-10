import pyautogui
import keyboard as keyb
import time
from settingGui import getSettings

state="К запуску готов!"

def hotKey():
  keyb.add_hotkey(getSettings().get("bindStartButton"), lambda: startBot())

  i = 0
  while(i == 0):
    if keyb.is_pressed(getSettings().get("bindEndButton")):
      print("Stop button was clicked")
      i = 1
      stopBot()

def stopBot():
  pass

def startBot():
  while(True):
    #Открывает меню, выбирает награды
    state="Открываю меню"
    # keyb.press_and_release("tab")
    state="Выбираю \"награды\""
    pyautogui.moveTo(1200, 35, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Выбирает ежедневные награды
    state="Выбираю \"Ежедневные награды\""
    pyautogui.moveTo(187, 107, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Забирает мульти кейс
    state="Забираю мульти кейс"
    pyautogui.moveTo(825, 325, duration=1)
    # pyautogui.click(clicks=1, interval=0.5)

    #Забирает новогодний кейс, если указал пользователь
    if getSettings().get("isSecondBox"):
      state="Забираю новогодний кейс"
      pyautogui.moveTo(1720, 325, duration=1)
      # pyautogui.click(clicks=1, interval=0.5)

    #Закрывает меню
    state="Закрываю меню"
    # keyb.press_and_release("tab")
  
    state="Жду 5 минут до следующего цикла"
    time.sleep(300) #Ждем 5 минут
