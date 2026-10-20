import customtkinter as ctk

app = ctk.CTk()
app.title("我的第一个软件")
app.geometry("400x300")

ctk.CTkLabel(app, text="点下面按钮试试").pack(pady=30)
ctk.CTkButton(app, text="点我").pack(pady=10)

app.mainloop()
