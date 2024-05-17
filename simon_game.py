import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import game_phase

class SimonGame:
    def __init__(self, root, difficulty="Facile", speed="Lent"):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.colors = {
            "R": "#FF0000",  # Rouge
            "G": "#00FF00",  # Vert
            "B": "#0000FF",  # Bleu
            "Y": "#FFFF00"   # Jaune
        }
        self.rectangles = {}
        self.sequence = self.generate_sequence(difficulty)
        #self.sequence = np.array(["B", "B", "B", "B"])
        self.current_index = 0
        self.opacity = 128  # Opacité de l'image
        self.speed(speed)

        # Création des rectangles
        self.create_rectangles()

        # Lancer la séquence après 3 secondes
        self.root.after(500, self.display_sequence)

        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def generate_sequence(self, difficulty):
        if difficulty == "Facile":
            return np.random.choice(list(self.colors.keys()), size=4)
        elif difficulty == "Moyen":
            return np.random.choice(list(self.colors.keys()), size=6)
        elif difficulty == "Difficile":
            return np.random.choice(list(self.colors.keys()), size=8)
        elif difficulty == "Giga Chad":
            return np.random.choice(list(self.colors.keys()), size=10)
        
    def speed(self, speed):
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
        # Diviser la fenêtre en quatre rectangles
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()

        for color, hex_color in self.colors.items():
            if color == "G" or color == "Y":
                x = 0
            else:
                x = w // 2
            if color == "G" or color == "R":
                y = 0
            else:
                y = h // 2
            rect = self.create_colored_rectangle(hex_color, w // 2, h // 2)
            rect.place(x=x, y=y)
            self.rectangles[color] = {"canvas": rect, "color": hex_color}

    # Fonction qui crée les 4 rectangles colorés
    def create_colored_rectangle(self, hex_color, width, height):
        color_with_opacity = hex_color + "{:02X}".format(self.opacity)
        image = Image.new("RGBA", (width, height), color_with_opacity)
        photo = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(self.root, width=width, height=height, bg="black", highlightthickness=0)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Garder une référence à l'image pour éviter la suppression par le garbage collector
        return canvas

    def display_sequence(self):
        self.display_next_color()

    def display_next_color(self):
        if self.current_index < len(self.sequence):
            color = self.sequence[self.current_index]
            self.highlight_rectangle(color)
            self.root.after(self.display_duration, self.reset_rectangles_and_wait)
            self.current_index += 1

    def highlight_rectangle(self, color):
        self.rectangles[color]["canvas"].config(bg=self.rectangles[color]["color"])

    def reset_rectangles_and_wait(self):
        self.reset_rectangles() # Enlève la couleur
        if self.current_index < len(self.sequence):
            self.root.after(self.pause_duration, self.display_next_color) # Pause avant de passer à la couleur suivante
        else:
            self.root.after(1000, self.process_user_input) # Pause de 1s avant de passer à la phase de jeu

    def reset_rectangles(self):
        for rect_color, rect_info in self.rectangles.items():
            rect_info["canvas"].config(bg="black")

    def process_user_input(self):
        self.root.destroy()  # Ferme la fenêtre du menu
        game_phase.compare_answers(len(self.sequence), self.sequence)