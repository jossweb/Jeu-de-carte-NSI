#import de modules externes
from tkinter import *
from tkinter import ttk
from json import loads
from random import randint

import customtkinter

# import de module internes au projet
import style
import time
from tkvideo import *


#def constantes
SIZE_WINDOW_WELCOME = [800, 400]
SIZE_WINDOW_GAME = [1000, 600]

#variable temporaire qui stock le choix du joueur 1 le temps que le joueur numéro
#prenne sa décision
card_on_table_player_1 = None


card_set_player_1 = None
card_set_player_2 = None

#variable accumulateur qui contienne le score de chaque joueurs
score_player_1 = 0
score_player_2 = 0

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

    window = create_window("home")
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
    global card_set_player_1, card_set_player_2
    global score_player_1, score_player_2

    if card_set_player_1 is None and card_set_player_2 is None:
        cards_dealt = cards_distribution(SET_CARDS)
        card_set_player_1 = cards_dealt[0]
        card_set_player_2 = cards_dealt[1]

    if card_on_table_player_1 is None:
        window = create_window("game")
        # création des scènes
        scene_1 = scene(1, score_player_1)

        scene_1.print(window)
        # appelle de la fonction qui place les boutons contenant les cartes à l'écran
        print_all_cards(card_set_player_1, window)
    else:
        window = create_window("game")
        scene_2 = scene(2, score_player_2)
        scene_2.print(window)
        # appelle de la fonction qui place les boutons contenant les cartes à l'écran
        print_all_cards(card_set_player_2, window)
    window.mainloop()


class scene:
    def __init__(self, player_number, score, player_name = "joueur"):
        self.player_name = player_name
        self.player_number = player_number
        self.score = score
    
    def print(self, window):
            if self.player_number == 1:
                 video_path = "videos/Séquence 01.mp4"
            else:
                 video_path = "videos/Séquence 02.mp4"
            video = Label(window)
            video.pack()
            player = tkvideo(video_path, video)
            player.play()
            text_label = Label(window, text= self.player_name, font=("Helvetica", 22), background="#FEB778")
            text_label.place(relx=0.5, rely=0.05, anchor="center")

            text_label = Label(window, text= self.score, font=("Helvetica", 26), foreground="#fff",background="#000")
            text_label.place(relx=0.955, rely=0.05, anchor="center")
class card:
    def __init__(self, name, score, path=None, image=None):
        self.name = name
        self.score = score
        self.path = path
        self.image = image

    def print(self, window, relx, rely, photo_image):
        if self.path is not None:
            text_label = Label(window)
            text_label.place(relx=relx, rely=rely, anchor="center")

            bouton_image = Button(text_label, image=photo_image, width=100, height=144, command= lambda: click_on_card(self.name, self.score, window))
            bouton_image.photo = photo_image  # Gardez une référence à l'image pour éviter la suppression par le garbage collector
            bouton_image.pack()
        else:
            return "Error: impossible to display content if path is not defined"

    def get_path(self):
         return f"images/cards/{self.name}.png"
    
def Deserialization_json(json_path):
    with open(json_path, "r") as fichier:
        json_data = fichier.read()
    return loads(json_data)

def create_window(type):
    """Cette fonction renvoie la fenêtre avec les paramètres qui 
    sont définis"""
    window = Tk()
    style.set_window_setting(window, type)
    window.resizable(False, False)
    return window

def cards_distribution(card_set):
    set_player_1 = []
    set_player_2 = []
    cards_count = len(card_set)
    for i in range(0, cards_count):
        if len(set_player_1) < cards_count / 2:
            if len(set_player_2) < cards_count / 2:
                rand = randint(1,2)
                if rand == 1:
                    set_player_1.append(card_set[i])
                else:
                    set_player_2.append(card_set[i])
            else:
                set_player_1.append(card_set[i])
        else:
            set_player_2.append(card_set[i])
    return(set_player_1, set_player_2)

def click_on_card(id_card, score_card, window):
    global card_on_table_player_1, card_set_player_2, score_player_1, score_player_2
    window.destroy()
    if card_on_table_player_1 is None:
        card_on_table_player_1 = (id_card, score_card) 
    else :
        if score_card < card_on_table_player_1[1]:
            score_player_1 += 2
        else:
            score_player_2 += 2
        card_on_table_player_1 = None
        card_set_player_2 = None
    main_game_page()
        

def print_all_cards(cards_set, window):
    """affiche le jeu de carte complet à l'écran pour le joueur"""
    num_cards = len(cards_set)
    # Liste pour stocker les instances de PhotoImage et eviter le garbage
    photo_images = []  
    for card_data in cards_set:
        card_instance = card(card_data[0], card_data[1])
        card_instance.path = card_instance.get_path()
        photo_image = PhotoImage(file=card_instance.path)
        photo_images.append(photo_image)
    
    if num_cards >= 20:
        cards_on_last_line = num_cards%10
        line = ((10 - cards_on_last_line + 1) / 2) / 10
        row = 0.70
        cards_on_last_line = num_cards%10
        for i, card_data in enumerate(cards_set):
            if i == cards_on_last_line: 
                line = 0.05
                row = 0.80
            elif i == cards_on_last_line + 10:
                row = 0.90
                line = 0.05
            card_instance = card(card_data[0], card_data[1])
            card_instance.path = card_instance.get_path()
            card_instance.print(window, line, row, photo_images[i])
            line += 0.1
    elif num_cards > 10:
        cards_on_last_line = num_cards%10
        line = ((10 - cards_on_last_line + 1) / 2) / 10
        row = 0.80
        for i, card_data in enumerate(cards_set):
            if i == cards_on_last_line: 
                line = 0.05
                row = 0.90
            card_instance = card(card_data[0], card_data[1])
            card_instance.path = card_instance.get_path()
            card_instance.print(window, line, row, photo_images[i])
            line += 0.1
    else :
        cards_on_last_line = num_cards%10
        line = ((10 - cards_on_last_line + 1) / 2) / 10
        row = 0.90
        for i, card_data in enumerate(cards_set):
            card_instance = card(card_data[0], card_data[1])
            card_instance.path = card_instance.get_path()
            card_instance.print(window, line, row, photo_images[i])
            line += 0.1

#exécution de la fonction principal au démarage
main_welcome_page()
