from tkinter import *

def create_principal_window():
    """Cette fonction revoie la fenêtre dont les paramètres sont
    défini"""
    window = Tk()
    set_window_setting(window)
    add_background(window)
    return window

def set_window_setting(window):
    """Cette fonction donne les paramètres à la fenêtre et prend 
    en paramètre la fenêtre"""
    window.title("Jeu de carte")
    window.geometry("1200x700")
    
def add_background(window):
    """ajoute une image au format ppm en fond de la page mise en 
    paramètre de cette fonction"""
    image = PhotoImage(file="plateau-en-bois.ppm")
    label = Label(window, image=image)
    label.place(x=0, y=0, relwidth=1, relheight=1)


window = create_principal_window()




# Lancer la boucle principale de la fenêtre
window.mainloop()
