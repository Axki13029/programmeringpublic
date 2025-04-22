import customtkinter as ctk
app = ctk.CTk()
app.geometry("500x300")
lista=[]
sträng=()
def buttonclick():    
    dialog=ctk.CTkInputDialog(text = "Skriv en sträng", title = "textanalys")
    sträng=(dialog.get_input())
    textbox.configure(text=sträng)
    textbox.update


button = ctk.CTkButton(app, text = "öppna textanalys verktyg", command = buttonclick)
button.pack(padx=20,pady=20)
textbox = ctk.CTkLabel(app, text="", text_color="white")
textbox.pack()
#textbox.insert("0.0", "sträng")
#text = textbox.get("0.0", "end")
#textbox.configure(state="disabled")
app.mainloop()

