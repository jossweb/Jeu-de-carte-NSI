
#modules externes
from json import loads
from tkinter import *

#modules internes au projet
from style import *

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