from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton
import json

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

def set_button_setting(click_link, window, style_json_path = None):
    """Cette fonction crée un bouton avec le module customtkinter
    et les attributs de styles qui sont donné au bouton"""
    button = CTkButton(window, command=click_link)
    
    if style_json_path is not None:
        style_button = Deserialization_json(style_json_path)

        # Configuraton du bouton avec les attributs du json
        button.configure(
            corner_radius=style_button.get("corner_radius", 0),
            border_width=style_button.get("border_width", 0),
            fg_color=style_button.get("fg_color", ""),
            hover_color=style_button.get("hover_color", "")
        )

    return button

def Deserialization_json(json_path):
    with open(json_path, "r") as fichier:
        json_data = fichier.read()
    return json.loads(json_data)