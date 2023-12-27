#import de modules externes
from tkinter import *
from tkinter import ttk

import customtkinter

# import de module internes au projet
import style
import back

#def constantes
SIZE_WINDOW_WELCOME = [1000, 600]
SIZE_WINDOW_GAME = [1920, 1080]

def play_button_click():
    main_game_page()

def main_welcome_page():
    """Fonction principal qui affiche les premières information à
    l'utilisateur. Cette fonction est exécuté au démarage du programme"""

    window = back.create_window("home")
    BACKGROUND_IMAGE = PhotoImage(file="plateau-en-bois.ppm")

    #création du Canvas
    canvas = Canvas(window, width=1000, height=600)
    canvas.pack()

    #ajout de l'image en background
    canvas.create_image(0, 0, anchor=NW, image=BACKGROUND_IMAGE)
    #ajout du texte de bienvenue
    canvas.create_text(500, 50, text="Bienvenue", font="calibri 45 italic", fill="white")

    button = style.set_button_setting(play_button_click, window, "json/style_button_play.json")
    canvas.create_window(500, 200, window=button)


    window.mainloop()

def main_game_page():
    window = back.create_window("game")

    BACKGROUND_IMAGE = PhotoImage(file="images/point de vue 1.png")

    #création du Canvas
    canvas = Canvas(window, width=1600, height=900)
    canvas.pack()

    #ajout de l'image en background
    canvas.create_image(0, 0, anchor=NW, image=BACKGROUND_IMAGE)

#exécution de la fonction principal au démarage
main_welcome_page()
