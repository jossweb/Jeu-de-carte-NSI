#import de modules externes
from tkinter import *

# import de module internes au projet
from style_entities import *

def create_principal_window():
    """Cette fonction renvoie la fenêtre dont les paramètres sont définis"""
    window = Tk()
    set_window_setting(window, "home")
    window.resizable(False, False)
    return window

window = create_principal_window()
background_image = PhotoImage(file="plateau-en-bois.ppm")
canvas = Canvas(window, width=1000, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=background_image)
canvas.create_text(500, 50, text="Bienvenue", font="calibri 40 bold", fill="white")

window.mainloop()
