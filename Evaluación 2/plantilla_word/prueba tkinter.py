import customtkinter as ctk

app= ctk.CTk()

app.title('UNA PANTALLA SDKSHDFLSHDFJ LOL')
app.geometry("720x720")

def on_boton_click():
    print("Boton presionado")

boton= ctk.CTkButton(app, text="haz click aqui", command=on_boton_click)
boton.pack(pady=20) 

app.mainloop()