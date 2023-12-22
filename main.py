
#import de modules externes
from tkinter import *

#import de module internes au projet
from style_entities import *

def create_principal_window():
    """Cette fonction revoie la fenêtre dont les paramètres sont
    défini"""
    window = Tk()
    set_window_setting(window, "home")
    window.resizable(False, False)
    return window


window = create_principal_window()
image = PhotoImage(file="plateau-en-bois.ppm")
label = Label(window, image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)
# Lancer la boucle principale de la fenêtre

add_label(window, )


window.mainloop()
