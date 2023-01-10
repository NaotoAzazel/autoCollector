import customtkinter
import json
import tkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

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

def settingsGui(root):
  window = customtkinter.CTkToplevel(root)

  window.geometry("400x270")
  window.title("Settings")

  frame = customtkinter.CTkFrame(master=window)
  frame.pack(pady=20, padx=60, fill="both", expand=True)

  label = customtkinter.CTkLabel(master=frame, text="Кнопка для запуска").pack()

  bindStartBtn = customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для запуска")
  bindStartBtn.pack(padx=12, pady=10)

  label2 = customtkinter.CTkLabel(master=frame, text="Кнопка для завершения").pack()

  bindEndBtn= customtkinter.CTkEntry(master=frame, placeholder_text="Кнопка для завершения")
  # bindEndBtn.insert(0, )
  bindEndBtn.pack(padx=12, pady=10)

  index = tkinter.BooleanVar()
  isSecondBox = customtkinter.CTkCheckBox(master=frame, text="Забирать новогодний кейс", variable=index).pack()
  
  applyBtn = customtkinter.CTkButton(master=frame, text="Сохранить изменения", command=lambda: applyChanges(window, bindStartBtn.get(), bindEndBtn.get(), index.get()))
  applyBtn.pack(padx=12, pady=10)

  window.mainloop()