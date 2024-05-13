import tkinter as tk
from simon_game import SimonGame

class MenuPage:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.difficulty = tk.StringVar(value="Moyen")
        self.speed = tk.StringVar(value="Normal")

        # Titre
        title_label = tk.Label(root, text="Menu", font=("Helvetica", 36))
        title_label.pack(pady=(100, 20))

        # Choix de la difficulté
        difficulty_frame = tk.Frame(root)
        difficulty_frame.pack(pady=10)

        difficulty_label = tk.Label(difficulty_frame, text="Difficulté:")
        difficulty_label.pack(side=tk.LEFT)

        difficulty_options = ["Facile", "Moyen", "Difficile", "Giga Chad"]
        for option in difficulty_options:
            radio_button = tk.Radiobutton(difficulty_frame, text=option, variable=self.difficulty, value=option)
            radio_button.pack(side=tk.LEFT, padx=10)

        # Choix de la rapidité
        speed_frame = tk.Frame(root)
        speed_frame.pack(pady=10)

        speed_label = tk.Label(speed_frame, text="Rapidité:")
        speed_label.pack(side=tk.LEFT)

        speed_options = ["Lent", "Normal", "Rapide", "Oeil de lynx"]
        for option in speed_options:
            radio_button = tk.Radiobutton(speed_frame, text=option, variable=self.speed, value=option)
            radio_button.pack(side=tk.LEFT, padx=10)

        # Bouton Commencer
        start_button = tk.Button(root, text="Commencer", command=self.start_game, font=("Helvetica", 18))
        start_button.pack(pady=20)

        # Bouton Quitter
        quit_button = tk.Button(root, text="Quitter", command=root.destroy, font=("Helvetica", 18))
        quit_button.pack()

    def start_game(self):
        self.root.destroy()  # Ferme la fenêtre du menu
        print("--------------------------------")
        print("Démarrage d'une partie")
        root = tk.Tk()
        game = SimonGame(root, difficulty=self.difficulty.get(), speed=self.speed.get())
        root.mainloop()