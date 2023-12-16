from tkinter import *

def create_principal_window():
    window = Tk()
    set_window_setting()

def set_window_setting():


# Créer la fenêtre principale


# on place l'image en background
image = PhotoImage(file="plateau-en-bois.ppm")  # Remplacez par le chemin de votre image en format PPM
label = Label(window, image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)



# Lancer la boucle principale de la fenêtre
window.mainloop()
