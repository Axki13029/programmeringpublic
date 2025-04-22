import customtkinter as ctk

def button_callback():
    if checkbox_1.get():
        while True:
            
            option1app = ctk.CTkToplevel()
            option1app = ctk.CTkLabel(option1app, text="Right choice", font=("Arial", 20))
            
            
            option1app.mainloop()                      
    if True:
        app = ctk.CTkInputDialog()
        app.title("wrong choice")
        app.geometry("1920*1080")
        app.grid_columnconfigure((1), weight=1)
        app.grid_rowconfigure((5), weight=9)
        app.geometry(1980*1080)
        

app = ctk.CTk()
app.title("my app")
app.geometry("1920*1080")
app.grid_columnconfigure((0), weight=1)


button = ctk.CTkButton(app, text="don't press", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_1 = ctk.CTkCheckBox(app, text="option1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = ctk.CTkCheckBox(app, text="option2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

app.mainloop()

