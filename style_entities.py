from tkinter import *
from PIL import Image, ImageTk

def set_window_setting(window, type):
    """Cette fonction donne les paramètres à la fenêtre et prend 
    en paramètre la fenêtre"""
    if (type == "home"):
        window.title("Jeu de carte")
        window_postion = get_window_start_position(window, 1000, 600)
        window.geometry(f"1000x600+{window_postion[0]}+{window_postion[1]}")
    elif(type == "game"):
        window.title("Jeu de carte")
        window_postion = get_window_start_position(window, 1920, 1080)
        window.geometry(f"1920x1080+{window_postion[0]}+{window_postion[1]}")
    else:
        print("ERROR : Window type is not defined or unknown")

def get_window_start_position(window, window_width, window_height):
    """Fonction qui renvoie une liste qui contient 2 entier qui vont 
    servir a placer la fenêtre au centre de l'écran de l'utilisateur"""
    #récupération de la taille de l'écran de l'utisateur en pixel
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    #ici l'on divise par 2 les longeurs précédentes et on leurs enlèvent
    #la moitié de la longeur de leurs axe (x ou y)
    return [(int(screen_width / 2)) - int(window_width / 2), (int(screen_height / 2)) - int(window_height / 2)]
    
def add_background(window):
    """ajoute une image au format ppm en fond de la page mise en 
    paramètre de cette fonction"""
    image = PhotoImage(file="plateau-en-bois.ppm")
    label = Label(window, image=image)
    label.place(x=0, y=0, relwidth=1, relheight=1)
