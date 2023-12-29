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

#carreau = T
#coeur = H
#piques = S
#Trèfle = C
SET_CARDS = [("CA", 14), ("C2", 2), ("C3", 3), ("C4", 4),
            ("C5", 5), ("C6", 6), ("C7", 7), ("C8", 8), ("C9", 9), ("C10", 10),
            ("CJ", 11), ("CQ", 12), ("CK", 13), ("HA", 14), ("H2", 2),
            ("H3", 3), ("H4", 4), ("H5", 5), ("H6", 5), ("H7", 7), ("H8", 8), 
            ("H9", 9), ("H10", 10), ("HJ", 11), ("HQ", 12), ("HK", 13),
            ("TA", 14), ("T2", 2), ("T3", 3), ("T4", 4), ("T5", 5), ("T6", 6),
            ("T7", 7), ("T8", 8), ("T9", 9), ("T10", 10), ("TJ", 11), ("TQ", 12),
            ("TK", 13), ("SA", 14), ("S2", 2), ("S3", 3), ("S4", 4),
            ("S5", 5), ("S6", 6), ("S7", 7), ("S8", 8), ("S9", 9), ("S10", 10),
            ("SJ", 11), ("SQ", 12), ("SK", 13)]

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
    cards_dealt = back.cards_distribution(SET_CARDS)
    cards_player_1 =  cards_dealt[0]
    cards_player_2 = cards_dealt[1]
    scene_1.print(window)

    test = back.card("C7", 10)
    test.path = test.get_path()
    test.print(window, lambda: clic_sur_bouton(), 0.5, 0.5)
    test.print(window, lambda: clic_sur_bouton(), 0.5, 0.8)
    window.mainloop()


#exécution de la fonction principal au démarage
main_welcome_page()
