#module qui permet d'afficher la vidéo dans un label
#Ce module est importer est modifier pour le projet.
#Il n'est donc pas créé de toute piece par le groupe pour
#le projet jeu de carte en NSI 

import tkinter as tk
import threading
import imageio
from PIL import Image, ImageTk

class tkvideo():
    """ 
        Main class of tkVideo. Handles loading and playing 
        the video inside the selected label.
        :path: 
            Path of video file
        :keyword label: 
            Name of label that will house the player
        :param size:
            Changes the video's dimensions (2-tuple, 
            default is 1000x600) 
    """
    def __init__(self, path, label, size=(1000,600)):
        self.path = path
        self.label = label
        self.size = size
    
    def load(self, path, label):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """
        frame_data = imageio.get_reader(path)
        while True:
            for image in frame_data.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                label.config(image=frame_image)
                label.image = frame_image

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.path, self.label))
        thread.daemon = 1
        thread.start()

#Changement par rapport au module de base:
#suppression du paramètre loop qui permet
#choisir si la vidéo sera diffusé à l'infini
#ou non (la vidéo sera donc obligatoirement diffusé en boucle)
#suppression du code qui affiche la vidéo qu'une seul fois
#passage en paramètre par défaut des valeurs en fonction
#des besoin du projet