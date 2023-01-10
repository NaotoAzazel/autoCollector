import customtkinter
from settingGui import settingsGui

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

state = "Нажимаю \"забрать награду\""

root = customtkinter.CTk()

root.geometry("300x100")
root.attributes("-topmost", True)
root.title("AutoCollector")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text=state)
label.pack(pady=12, padx=10)

startBtn = customtkinter.CTkButton(master=frame, text="Start", width=10)
startBtn.pack(pady=0, padx=0)
startBtn.place(x=180, y=40)

settingBtn = customtkinter.CTkButton(master=frame, text="Settings", width=10, command=lambda: settingsGui(root))
settingBtn.pack(pady=0, padx=0)
settingBtn.place(x=110, y=40)

root.mainloop()