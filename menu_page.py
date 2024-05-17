import tkinter as tk
from simon_game import SimonGame

class MenuPage:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Définir la fenêtre en plein écran
        self.difficulty = tk.StringVar(value="Moyen")  # Variable pour stocker la difficulté choisie
        self.speed = tk.StringVar(value="Normal")  # Variable pour stocker la rapidité choisie

        # Titre
        title_label = tk.Label(root, text="Menu", font=("Helvetica", 36)) # Affiche Menu
        title_label.pack(pady=(100, 20))  # Afficher le titre avec un espacement

        # Choix de la difficulté
        difficulty_frame = tk.Frame(root)  # Créer un cadre pour les options de difficulté
        difficulty_frame.pack(pady=10)  # Afficher le cadre avec un espacement

        difficulty_label = tk.Label(difficulty_frame, text="Difficulté:")  # Label
        difficulty_label.pack(side=tk.LEFT)

        difficulty_options = ["Facile", "Moyen", "Difficile", "Giga Chad"]  # Options de difficulté disponibles
        for option in difficulty_options:
            radio_button = tk.Radiobutton(difficulty_frame, text=option, variable=self.difficulty, value=option)  # Bouton radio pour chaque option de difficulté
            radio_button.pack(side=tk.LEFT, padx=10)  # Afficher les boutons radio avec un espacement

        # Choix de la rapidité
        speed_frame = tk.Frame(root)  # Créer un cadre pour les options de rapidité
        speed_frame.pack(pady=10)  # Espacement

        speed_label = tk.Label(speed_frame, text="Rapidité:")  # Label
        speed_label.pack(side=tk.LEFT)

        speed_options = ["Lent", "Normal", "Rapide", "Oeil de lynx"]  # Options de rapidité disponibles
        for option in speed_options:
            radio_button = tk.Radiobutton(speed_frame, text=option, variable=self.speed, value=option)  # Bouton radio pour chaque option de rapidité
            radio_button.pack(side=tk.LEFT, padx=10)  # Afficher les boutons radio avec un espacement

        # Bouton Commencer
        start_button = tk.Button(root, text="Commencer", command=self.start_game, font=("Helvetica", 18))  # Bouton pour démarrer le jeu
        start_button.pack(pady=20)  # Afficher le bouton avec un espacement

        # Bouton Quitter
        quit_button = tk.Button(root, text="Quitter", command=root.destroy, font=("Helvetica", 18))  # Bouton pour quitter l'application
        quit_button.pack()  # Afficher le bouton

    # Démarrer le jeu en créant une instance de SimonGame avec les options sélectionnées
    def start_game(self):
        self.root.destroy()  # Fermer la fenêtre du menu
        print("--------------------------------")
        print("Démarrage d'une partie")
        root = tk.Tk()  # Créer une nouvelle fenêtre
        game = SimonGame(root, difficulty=self.difficulty.get(), speed=self.speed.get())  # Démarrer une partie avec les options choisies
        root.mainloop()  # Lancer la boucle principale de la fenêtre
