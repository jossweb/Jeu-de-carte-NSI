
#modules externes
from json import loads
from tkinter import *

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
     def __init__(self, name, score, path):
        self.name = name
        self.score = score
        
class card_set:
     def __init__(self, path):
          self.cards = [["CA", "C2", "C3", "C4","C5", "C6", "C7", "C8",
                         "C9", "C10", "CV", "CD", "CR"],
                         ["HA", "H2", "H3", "H4","H5", "H6", "H7", "H8",
                         "H9", "H10", "HV", "HD", "HR"],
                         ["TA", "T2", "T3", "T4","T5", "T6", "T7", "T8",
                         "T9", "T10", "TV", "TD", "TR"],
                         ["SA", "S2", "S3", "S4","S5", "S6", "S7", "S8",
                         "S9", "S10", "SV", "SD", "SR"],]
          self.path = "cards/"
          self.score = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

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