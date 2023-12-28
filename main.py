#import de modules externes
from tkinter import *
from tkinter import ttk

import customtkinter

# import de module internes au projet
import style
import back
import time

#def constantes
SIZE_WINDOW_WELCOME = [800, 400]
SIZE_WINDOW_GAME = [1000, 600]

SET_CARDS = ["CA", "C2", "C3", "C4","C5", "C6", "C7", "C8", "C9", "C10", "CV", "CD", "CR", "HA", "H2", "H3", "H4","H5", "H6", "H7", "H8", "H9", "H10", "HV", "HD", "HR", "TA", "T2", "T3", "T4","T5", "T6", "T7", "T8", "T9", "T10", "TV", "TD", "TR", "SA", "S2", "S3", "S4","S5", "S6", "S7", "S8", "S9", "S10", "SV", "SD", "SR"]

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

def clic_sur_bouton():
    print("touch !")

def main_game_page():
    window = back.create_window("game")
    #création des scènes
    scene_1 = back.scene(1)
    scene_2 = back.scene(2)
    cards_dealt = back.cards_distribution(SET_CARDS)
    cards_player_1 =  cards_dealt[0]
    cards_player_2 = cards_dealt[1]
    scene_1.print(window)
    window.mainloop()


#exécution de la fonction principal au démarage
main_welcome_page()
