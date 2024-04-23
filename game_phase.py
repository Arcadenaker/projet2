import serial
import tkinter as tk

def lire_donnees(nombre_mesures):
    donnees = []
    with serial.Serial("COM8", 9600) as ser:
        for _ in range(nombre_mesures):
            donnees.append(ser.readline().strip().decode('utf-8'))
    return donnees

"""
# Pour tester sans Arduino
def lire_donnees(nombre_mesures):
    return [input() for _ in range(nombre_mesures)]
"""

class UserInput:
    def __init__(self, root, sequence):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.sequence = sequence

        # Afficher "En attente de votre combinaison"
        self.attente_label = tk.Label(root, text="En attente de votre combinaison...", font=("Helvetica", 25))
        self.attente_label.pack(pady=150)

        # Bouton pour abandonner
        stop_button = tk.Button(root, text="Abandonner", command=self.go_menu, font=("Helvetica", 18))
        stop_button.pack(pady=5)

        # Lire la combinaison de l'utilisateur
        self.root.after(1000, self.check_input)

    def check_input(self):
        self.user_sequence = lire_donnees(len(self.sequence))
        if self.user_sequence:
            # Si l'utilisateur a entré sa combinaison, afficher les résultats
            self.display_results(self.sequence == self.user_sequence)
        else:
            # Sinon, continuer à attendre
            self.attente_label.pack(pady=150)
            self.root.after(1000, self.check_input)

    def display_results(self, is_correct):
        # Refais une page vierge
        for widget in self.root.winfo_children():
            widget.destroy()

        # Afficher les résultats avec fond vert ou rouge en fonction du résultat
        if False in is_correct:
            background_color = "red"
            result_message = "Désolé, tu as échoué."
        else:
            background_color = "green"
            result_message = "Bravo! Tu as réussi!"

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