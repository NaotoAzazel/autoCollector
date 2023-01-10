import pyautogui
import keyboard as keyb
import time

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
