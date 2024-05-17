import serial
import tkinter as tk
import numpy as np

# Fonction pour lire les données depuis le port série (discussion par usb avec l'arduino)
def lire_donnees(nombre_mesures, correct_answer):
    donnees = []
    print("En attente de la combinaison...")
    with serial.Serial("COM10", 9600) as ser:  # Ouvrir le port série pour la communication
        for i in range(nombre_mesures):
            color = ser.readline().decode().strip()  # Ecoute jusqu'à ce qu'une couleur soit reçue
            donnees.append(color)  # Ajouter la couleur lue à la liste des données
            if correct_answer[i] != color:  # Vérifier si la couleur lue correspond à la réponse correcte
                return donnees  # Retourner les données si la réponse est incorrecte
            print("Reçu:", color)  # Afficher la couleur lue en console
    return donnees  # Retourne la liste

# Fonction de test (quand on ne peut pas utiliser le port série)
def test_lire_donnees(n, correct_answer):
    donnees = []
    print("En attente de la combinaison...")
    for i in range(n):
        color = input("Entrez une couleur: ")
        donnees.append(color)
        if correct_answer[i] != color:
            return donnees 
        print("Reçu:", color)
    return donnees

# Fonction pour comparer les réponses de l'utilisateur avec la réponse correcte
def compare_answers(n, correct_answer):
    answers = np.array(lire_donnees(n, correct_answer))  # Lire les réponses de l'utilisateur
    #answers = np.array(test_lire_donnees(n, correct_answer))
    print("Réponse de l'utilisateur:", answers)  # Afficher les réponses de l'utilisateur
    print("Réponse correcte:", correct_answer)  # Afficher la réponse correcte
    if answers.size != correct_answer.size:  # Vérifier si le nombre de réponses est différent de la réponse correcte
        return show_results(False, correct_answer) # Afficher les résultats avec une réponse incorrecte
    result = all(answers == correct_answer)  # Vérifier si toutes les réponses sont correctes
    show_results(result, correct_answer)  # Afficher les résultats

# Fonction pour afficher les résultats
def show_results(result, correct_answer):
    print("Affichage des résultats...")
    root = tk.Tk()  # Créer une nouvelle instance Tkinter
    root.title("Résultats")  # Définir le titre de la fenêtre
    root.attributes('-fullscreen', True)  # Définir la fenêtre en plein écran

    if result:  # Si les réponses sont correctes
        background_color = "green"  # Couleur de fond verte
        result_message = "FÉLICITATIONS!"  # Message de résultat
    else:  # Si les réponses sont incorrectes
        background_color = "red"  # Couleur de fond rouge
        result_message = "GAME OVER"  # Message de résultat

    # Créer un cadre pour afficher les résultats avec un fond coloré
    result_frame = tk.Frame(root, bg=background_color)
    result_frame.pack(fill=tk.BOTH, expand=True)

    # Afficher le message de résultat au centre du cadre
    label = tk.Label(result_frame, text=result_message, font=("Helvetica", 40), bg=background_color, fg="white")
    label.pack(pady=(100, 20))
    if not result:
        label2 = tk.Label(result_frame, text=f"Tu n'es pas très fort", font=("Helvetica", 20), bg=background_color, fg="white")
        label2.pack(pady=10)

    # Bouton pour retourner au menu principal
    stop_button = tk.Button(result_frame, text="Retour au menu", command=lambda: go_menu(root), font=("Helvetica", 18))
    stop_button.pack(pady=5)

# Fonction pour revenir au menu principal
def go_menu(root):
    from menu_page import MenuPage  # Importer la classe MenuPage
    print("Fin de la partie")
    root.destroy()  # Fermer la fenêtre des résultats
    root = tk.Tk()  # Créer une nouvelle instance Tkinter
    menu = MenuPage(root)  # Recommencer à l'infini et dans l'au-delà
    root.mainloop()