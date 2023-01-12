import pyautogui
from Utils import getSettings
import time


state = {0: "Готов к запуску!", 1: "Открываю меню", 2: "Выбираю \"награды\"", 3: "Выбираю \"Ежедневные награды\"", 4: "Забираю мульти кейс", 5: "Закрываю меню", 6: "Жду 5 минут до следующего цикла", 7: "Забираю новогодний кейс"}
counter = 0
saveBack = 0

def startBot():
  global counter, saveBack
  while(True):
    #Открывает меню, выбирает награды
    counter += 1
    keyb.press_and_release("tab")
    counter += 1
    pyautogui.moveTo(1200, 35, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    #Выбирает ежедневные награды
    counter += 1
    pyautogui.moveTo(187, 107, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    #Забирает мульти кейс
    counter += 1
    pyautogui.moveTo(825, 325, duration=1)
    pyautogui.click(clicks=1, interval=0.5)

    saveBack = counter

    #Забирает новогодний кейс, если указал пользователь
    if getSettings().get("isSecondBox"):
      pyautogui.moveTo(1720, 325, duration=1)
      counter = 7
      pyautogui.click(clicks=1, interval=0.5)

    counter = saveBack

    #Закрывает меню
    counter += 1
    keyb.press_and_release("tab")

    # state="Жду 5 минут до следующего цикла"
    counter += 1
    time.sleep(300) #Ждем 5 минут
    counter = 0


