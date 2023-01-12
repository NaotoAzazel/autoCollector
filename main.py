import customtkinter
import keyboard as keyb
import Utils
import Bot

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

def changeText():
  statusBar.configure(text=Bot.state[Bot.counter])
  root.after(500, changeText)

def settingsGui():
  window = customtkinter.CTkToplevel(root)

  window.geometry("400x270")
  window.title("Settings")

  frame = customtkinter.CTkFrame(master=window)
  frame.pack(pady=20, padx=60, fill="both", expand=True)

  label = customtkinter.CTkLabel(master=frame, text="Кнопка для запуска").pack()

  bindStartBtn = customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для запуска")
  bindStartBtn.pack(padx=12, pady=10)
  bindStartBtn.insert(0, Utils.getSettings().get("bindStartButton"))

  label2 = customtkinter.CTkLabel(master=frame, text="Кнопка для завершения").pack()

  bindEndBtn= customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для завершения")
  bindEndBtn.insert(0, Utils.getSettings().get("bindEndButton"))
  bindEndBtn.pack(padx=12, pady=10)

  index = customtkinter.BooleanVar(value=Utils.getSettings().get("isSecondBox"))
  isSecondBox = customtkinter.CTkCheckBox(master=frame, text="Забирать новогодний кейс", variable=index, onvalue=True, offvalue=False).pack()

  applyBtn = customtkinter.CTkButton(master=frame, text="Сохранить изменения", command=lambda: Utils.applyChanges(window, bindStartBtn.get(), bindEndBtn.get(), index.get()))
  applyBtn.pack(padx=12, pady=10)

  window.mainloop()

root = customtkinter.CTk()

root.geometry("300x100")
root.attributes("-topmost", True)
root.title("AutoCollector")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

statusBar = customtkinter.CTkLabel(master=frame, text="Status")
statusBar.pack(pady=0, padx=0)

startBtn = customtkinter.CTkButton(master=frame, text="Start", width=10, command= lambda: keyb.add_hotkey(Utils.getSettings().get("bindStartButton"), lambda: Bot.startBot()))
startBtn.pack(pady=0, padx=0)
startBtn.place(x=180, y=40)

settingBtn = customtkinter.CTkButton(master=frame, text="⚙", width=10, command=settingsGui, fg_color="gray")
settingBtn.pack(pady=0, padx=0)
settingBtn.place(x=140, y=40)

changeText()
root.mainloop()
