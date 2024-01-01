import tkinter as tk
import imageio
from PIL import Image, ImageTk

class tkvideo():
    def __init__(self, path, label, size=(1000,600)):
        self.path = path
        self.label = label
        self.size = size
        self.frame_data = imageio.get_reader(path)
        self.image_list = []
        self.current_frame = 0

    def load(self):
        try:
            image = self.frame_data.get_data(self.current_frame)
            frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
            self.label.config(image=frame_image)
            self.label.image = frame_image
            self.current_frame = (self.current_frame + 1) % len(self.frame_data)
            self.label.after(30, self.load)  # Met à jour l'image toutes les 30 millisecondes (ou ajustez selon vos besoins)
        except:
            pass

    def play(self):
        self.load()

# Utilisation :
# player = tkvideo("videos/Séquence 01.mp4", label)
# player.play()
