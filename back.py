
#modules externes
from json import loads
from tkinter import *
from random import randint

#modules internes au projet
from style import *
from tkvideo import *

class scene:
    def __init__(self, player_number, score = 0, player_name = "joueur"):
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

    def print(self, window, click, relx, rely, photo_image):
        if self.path is not None:
            text_label = Label(window)
            text_label.place(relx=relx, rely=rely, anchor="center")

            bouton_image = Button(text_label, image=photo_image, width=100, height=144, command=click)
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
    set_window_setting(window, type)
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

def click_on_card():
    pass

def print_all_cards(cards_set, window):
    # Liste pour stocker les instances de PhotoImage
    photo_images = []  
    for card_data in cards_set:
        card_instance = card(card_data[0], card_data[1])
        card_instance.path = card_instance.get_path()
        photo_image = PhotoImage(file=card_instance.path)
        photo_images.append(photo_image)

    for i, card_data in enumerate(cards_set):
        card_instance = card(card_data[0], card_data[1])
        card_instance.path = card_instance.get_path()
        card_instance.print(window, lambda: click_on_card(), 0.05 + (0.05 * i), 0.5, photo_images[i])
