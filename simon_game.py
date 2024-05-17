import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import game_phase

class SimonGame:
    def __init__(self, root, difficulty="Facile", speed="Lent"):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Définir la fenêtre en plein écran
        # Couleurs disponibles pour les rectangles
        self.colors = {
            "R": "#FF0000",  # Rouge
            "G": "#00FF00",  # Vert
            "B": "#0000FF",  # Bleu
            "Y": "#FFFF00"   # Jaune
        }
        self.rectangles = {}  # Dictionnaire pour stocker les rectangles
        # Générer une séquence de couleurs en fonction de la difficulté choisie
        self.sequence = self.generate_sequence(difficulty)
        self.current_index = 0  # Index actuel dans la séquence
        self.opacity = 128  # Opacité de l'image pour les rectangles
        self.speed(speed)  # Définir la vitesse du jeu

        # Créer les rectangles colorés
        self.create_rectangles()

        # Démarrer la séquence après 0.5 seconde
        self.root.after(500, self.display_sequence)

        # Lier la touche "Échap" à la fermeture de la fenêtre
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def generate_sequence(self, difficulty):
        # Générer une séquence de couleurs en fonction de la difficulté
        if difficulty == "Facile":
            return np.random.choice(list(self.colors.keys()), size=4)
        elif difficulty == "Moyen":
            return np.random.choice(list(self.colors.keys()), size=6)
        elif difficulty == "Difficile":
            return np.random.choice(list(self.colors.keys()), size=8)
        elif difficulty == "Giga Chad":
            return np.random.choice(list(self.colors.keys()), size=10)
        
    def speed(self, speed):
        # Définir la vitesse du jeu en fonction du paramètre "speed"
        if speed == "Lent":
            self.display_duration = 1000
            self.pause_duration = 1000
        elif speed == "Normal":
            self.display_duration = 650
            self.pause_duration = 650
        elif speed == "Rapide":
            self.display_duration = 350
            self.pause_duration = 350
        elif speed == "Oeil de lynx":
            self.display_duration = 175
            self.pause_duration = 175

    def create_rectangles(self):
        # Créer les rectangles colorés dans la fenêtre
        w = self.root.winfo_screenwidth()  # Largeur de l'écran
        h = self.root.winfo_screenheight()  # Hauteur de l'écran

        # Parcourir les couleurs et créer les rectangles correspondants
        for color, hex_color in self.colors.items():
            # Positionner les rectangles en fonction de leur couleur
            if color == "G" or color == "Y":
                x = 0
            else:
                x = w // 2
            if color == "G" or color == "R":
                y = 0
            else:
                y = h // 2
            # Créer le rectangle coloré et le placer dans la fenêtre
            rect = self.create_colored_rectangle(hex_color, w // 2, h // 2)
            rect.place(x=x, y=y)
            # Stocker le rectangle dans le dictionnaire des rectangles
            self.rectangles[color] = {"canvas": rect, "color": hex_color}

    # Créer un rectangle coloré avec une opacité
    def create_colored_rectangle(self, hex_color, width, height):
        # Ajouter l'opacité à la couleur spécifiée
        color_with_opacity = hex_color + "{:02X}".format(self.opacity)
        # Créer une nouvelle image avec la couleur et l'opacité spécifiées
        image = Image.new("RGBA", (width, height), color_with_opacity)
        # Convertir l'image en un format compatible avec Tkinter
        photo = ImageTk.PhotoImage(image)
        # Créer un canevas Tkinter pour afficher l'image
        canvas = tk.Canvas(self.root, width=width, height=height, bg="black", highlightthickness=0)
        # Créer une image sur le canevas à partir de l'image convertie
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        # Conserver une référence à l'image pour éviter qu'elle ne soit supprimée par le garbage collector
        canvas.image = photo  
        return canvas

    # Afficher la séquence de couleurs
    def display_sequence(self):
        self.display_next_color()

    # Afficher la couleur suivante dans la séquence
    def display_next_color(self):
        if self.current_index < len(self.sequence):
            color = self.sequence[self.current_index]
            self.highlight_rectangle(color)  # Mettre en surbrillance le rectangle correspondant à la couleur
            self.root.after(self.display_duration, self.reset_rectangles_and_wait)  # Réinitialiser les rectangles après un délai
            self.current_index += 1

    # Mettre en surbrillance le rectangle correspondant à une couleur
    def highlight_rectangle(self, color):
        self.rectangles[color]["canvas"].config(bg=self.rectangles[color]["color"])

    # Réinitialiser les rectangles et attendre avant d'afficher la couleur suivante
    def reset_rectangles_and_wait(self):
        self.reset_rectangles()  # Réinitialiser les rectangles en enlevant la couleur
        if self.current_index < len(self.sequence):
            self.root.after(self.pause_duration, self.display_next_color)  # Attendre avant d'afficher la couleur suivante
        else:
            self.root.after(1000, self.process_user_input)  # Attendre 1 seconde avant de passer à la phase de jeu

    # Réinitialiser les couleurs des rectangles
    def reset_rectangles(self):
        for rect_color, rect_info in self.rectangles.items():
            rect_info["canvas"].config(bg="black")

    # Traiter l'entrée de l'utilisateur après l'affichage de la séquence
    def process_user_input(self):
        self.root.destroy()  # Fermer la fenêtre du menu
        game_phase.compare_answers(len(self.sequence), self.sequence)  # Comparer la séquence de l'utilisateur avec celle générée