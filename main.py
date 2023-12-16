from tkinter import *

def create_principal_window():
    """Cette fonction revoie la fenêtre dont les paramètres sont
    défini"""
    window = Tk()
    set_window_setting(window)
    window.resizable(False, False)
    return window

def set_window_setting(window):
    """Cette fonction donne les paramètres à la fenêtre et prend 
    en paramètre la fenêtre"""
    window.title("Jeu de carte")
    window_postion = get_window_start_position(window)
    window.geometry(f"1600x800+{window_postion[0]}+{window_postion[1]}")

def get_window_start_position(window):
    """Fonction qui renvoie une liste qui contient 2 entier qui vont 
    servir a placer la fenêtre au centre de l'écran de l'utilisateur"""
    #récupération de la taille de l'écran de l'utisateur en pixel
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    #ici l'on divise par 2 les longeurs précédentes et on leurs enlèvent
    #la moitié de la longeur de leurs axe (x ou y)
    return [(int(screen_width / 2)) - 800, (int(screen_height / 2)) - 400]
    
def add_background(window):
    """ajoute une image au format ppm en fond de la page mise en 
    paramètre de cette fonction"""
    image = PhotoImage(file="plateau-en-bois.ppm")
    label = Label(window, image=image)
    label.place(x=0, y=0, relwidth=1, relheight=1)


window = create_principal_window()
image = PhotoImage(file="plateau-en-bois.ppm")
label = Label(window, image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Lancer la boucle principale de la fenêtre
window.mainloop()
