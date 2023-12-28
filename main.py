#import de modules externes
from tkinter import *
from tkinter import ttk

import customtkinter

# import de module internes au projet
import style
import back

#def constantes
SIZE_WINDOW_WELCOME = [800, 400]
SIZE_WINDOW_GAME = [1000, 600]

def play_button_click(window):
    window.destroy()
    main_game_page()

def main_welcome_page():
    """Fonction principal qui affiche les premières information à
    l'utilisateur. Cette fonction est exécuté au démarage du programme"""

    window = back.create_window("home")
    BACKGROUND_IMAGE = PhotoImage(file="plateau-en-bois.ppm")

    #création du Canvas
    canvas = Canvas(window, width=800, height=400)
    canvas.pack()

    #ajout de l'image en background
    canvas.create_image(0, 0, anchor=NW, image=BACKGROUND_IMAGE)
    #ajout du texte de bienvenue
    canvas.create_text(400, 50, text="Bienvenue", font="calibri 45 italic", fill="white")

    button = style.set_button_setting(lambda: play_button_click(window), window, "json/style_button_play.json")
    canvas.create_window(400, 200, window=button)
    window.mainloop()

def main_game_page():
    window = back.create_window("game")
    #création des scènes
    scene_1 = back.scene(1)
    scene_2 = back.scene(2)

    scene_1.print(window)

    window.mainloop()


#exécution de la fonction principal au démarage
main_welcome_page()
