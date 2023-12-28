
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
    def __init__(self, name, score, path = None):
        self.name = name
        self.score = score
        self.path = path

    def print(self, window, click):
        if self.get_path is not None:
            text_label = Label(window)
            text_label.place(relx=0.5, rely=0.8, anchor="center")
            image = PhotoImage(file=self.path, name="card")
            bouton_image = Button(text_label, image=image, width=150, height=230,command= click)
            bouton_image.pack()
        else: 
             return "Error : impossible to display content if path is not defined"
          
    def get_path(self):
         return f"cards/{self.name}.png"
         
class card_set_player:
     def __init__(self, cards):
          self.cards = cards

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
