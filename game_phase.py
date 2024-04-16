import serial
import tkinter as tk

def lire_donnees(nombre_mesures):
    donnees = []
    with serial.Serial("COM6", 9600) as ser:
        for _ in range(nombre_mesures):
            donnees.append(ser.readline().strip().decode('utf-8'))
    return donnees

class UserInput:
    def __init__(self, root, sequence):
        self.root = root
        self.root.attributes('-fullscreen', True)

        label = tk.Label(root, text="Attente de ta combinaison...", font=("Helvetica", 25))
        label.pack(pady=150)

        stop_button = tk.Button(root, text="Abandonner", command=self.go_menu, font=("Helvetica", 18))
        stop_button.pack(pady=5)

        self.sequence = sequence
        print(self.sequence)
        self.user_sequence = lire_donnees(len(sequence))
        self.is_correct = self.sequence == self.user_sequence

        self.display_results(self.is_correct)

    def display_results(self, is_correct):
        # Refais une page vierge
        for widget in self.root.winfo_children():
            widget.destroy()

        # Afficher les résultats avec fond vert ou rouge en fonction du résultat
        if is_correct.any():
            background_color = "green"
            result_message = "Bravo! Tu as réussi!"
        else:
            background_color = "red"
            result_message = "Désolé, tu as échoué."

        # Créer un cadre pour afficher les résultats avec fond vert ou rouge
        result_frame = tk.Frame(self.root, bg=background_color)
        result_frame.pack(fill=tk.BOTH, expand=True)

        # Afficher le message de résultat au centre du cadre
        label = tk.Label(result_frame, text=result_message, font=("Helvetica", 25))
        label.pack(pady=5)

        # Bouton pour retourner au menu
        stop_button = tk.Button(result_frame, text="Retour au menu", command=self.go_menu, font=("Helvetica", 18))
        stop_button.pack(pady=5)

    def go_menu(self):
        from menu_page import MenuPage
        self.root.destroy()  # Ferme la fenêtre du menu
        root = tk.Tk()
        menu = MenuPage(root)
        root.mainloop()