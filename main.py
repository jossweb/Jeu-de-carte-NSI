#import de modules externes
from tkinter import *
from tkinter import ttk

import customtkinter

# import de module internes au projet
from style import *

def create_principal_window():
    """Cette fonction renvoie la fenêtre dont les paramètres sont définis"""
    window = Tk()
    set_window_setting(window, "home")
    window.resizable(False, False)
    return window

def on_button_click():
    print("Bouton cliqué !")

window = create_principal_window()
BACKGROUND_IMAGE = PhotoImage(file="plateau-en-bois.ppm")

#création du Canvas
canvas = Canvas(window, width=1000, height=600)
canvas.pack()

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), 
                padding=10, borderwidth=5, relief="flat", 
                bordercolor="gray", borderround=10)

#ajout de l'image en background
canvas.create_image(0, 0, anchor=NW, image=BACKGROUND_IMAGE)
#ajout du texte de bienvenue
canvas.create_text(500, 50, text="Bienvenue", font="calibri 45 italic", fill="white")

button = set_button_setting(on_button_click, window, "json/style_button_play.json")
canvas.create_window(500, 200, window=button)


window.mainloop()
