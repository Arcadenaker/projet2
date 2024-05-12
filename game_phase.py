import serial
import tkinter as tk

class ColorDisplayWindow:
    def __init__(self, color):
        # Création de la fenêtre
        self.root = tk.Toplevel()
        self.root.title("Couleur Sélectionnée")
        self.root.geometry("300x200")

        # Label pour afficher la couleur sélectionnée
        self.color_label = tk.Label(self.root, text=f"Couleur sélectionnée: {color}", font=("Helvetica", 20))
        self.color_label.pack(pady=50)

        # Fermer automatiquement la fenêtre après quelques secondes
        self.root.after(1500, self.close_window)

    def close_window(self):
        # Ferme la fenêtre
        self.root.destroy()

def lire_donnees(nombre_mesures):
    donnees = []
    with serial.Serial("COM12", 9600) as ser:
        for _ in range(nombre_mesures):
            color = ser.readline().decode().strip()
            donnees.append(color)
            ColorDisplayWindow(color)
            print("Reçu:", color)
    return donnees

# Pour tester sans Arduino
def test_function(nombre_mesures):
    colors = []
    for _ in range(nombre_mesures):
        color = input("Entrez une couleur: ")
        ColorDisplayWindow(color)
        colors.append(color)
    return colors


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
        # Lire la combinaison de l'utilisateur
        self.user_sequence = lire_donnees(len(self.sequence))
        #self.user_sequence = test_function(len(self.sequence))

        if self.user_sequence:
            # Si l'utilisateur a entré sa combinaison, afficher les résultats
            self.display_results(self.sequence == self.user_sequence)
            print("Bonne combinaison:", self.sequence, "|", "Combinaison de l'utilisateur:", self.user_sequence)
        else:
            # Sinon, continuer à attendre
            self.attente_label.pack(pady=150)
            self.root.after(1000, self.check_input)

    def display_results(self, is_correct):
        # Refais une page vierge
        for widget in self.root.winfo_children():
            widget.destroy()

        # Afficher les résultats avec fond vert ou rouge en fonction du résultat
        if is_correct:
            background_color = "green"
            result_message = "Bravo! La combinaison est correcte!"
        else:
            background_color = "red"
            result_message = "La combinaison est incorrecte."

        # Créer un cadre pour afficher les résultats avec fond vert ou rouge
        result_frame = tk.Frame(self.root, bg=background_color)
        result_frame.pack(fill=tk.BOTH, expand=True)

        # Afficher le message de résultat au centre du cadre
        label = tk.Label(result_frame, text=result_message, font=("Helvetica", 25), bg=background_color)
        label.pack(pady=(100, 20))

        # Bouton pour retourner au menu
        stop_button = tk.Button(result_frame, text="Retour au menu", command=self.go_menu, font=("Helvetica", 18))
        stop_button.pack(pady=5)

    def go_menu(self):
        from menu_page import MenuPage
        self.root.destroy()  # Ferme la fenêtre du menu
        root = tk.Tk()
        menu = MenuPage(root) 
        root.mainloop()