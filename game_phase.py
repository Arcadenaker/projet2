import serial
import tkinter as tk
import numpy as np

def lire_donnees(nombre_mesures, correct_answer):
    donnees = []
    print("En attente de la combinaison...")
    with serial.Serial("COM10", 9600) as ser:
        for i in range(nombre_mesures):
            color = ser.readline().decode().strip()
            donnees.append(color)
            if correct_answer[i] != color:
                return donnees
            print("Reçu:", color)
    return donnees

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

def compare_answers(n, correct_answer):
    answers = lire_donnees(n, correct_answer)
    #answers = np.array(test_lire_donnees(n, correct_answer))
    print("Réponse de l'utilisateur:", answers)
    print("Réponse correcte:", correct_answer)
    if answers.size != correct_answer.size:
        return show_results(False, correct_answer)
    print(answers)
    print(correct_answer)
    result = all(answers == correct_answer)
    print("Réussi?:", result)
    show_results(result, correct_answer)

def show_results(result, correct_answer):
    print("Affichage des résultats...")
    root = tk.Tk()
    root.title("Résultats")
    root.attributes('-fullscreen', True)

    if result:
        background_color = "green"
        result_message = "FÉLICITATIONS!"
    else:
        background_color = "red"
        result_message = "GAME OVER"

    # Créer un cadre pour afficher les résultats avec fond vert ou rouge
    result_frame = tk.Frame(root, bg=background_color)
    result_frame.pack(fill=tk.BOTH, expand=True)

    # Afficher le message de résultat au centre du cadre
    label = tk.Label(result_frame, text=result_message, font=("Helvetica", 40), bg=background_color, fg="white")
    label.pack(pady=(100, 20))
    if not result:
        label2 = tk.Label(result_frame, text=f"La couleur correcte était la couleur correcte était {correct_answer[len(correct_answer) - 1]}", font=("Helvetica", 20), bg=background_color, fg="white")
        label2.pack(pady=10)

    # Bouton pour retourner au menu
    stop_button = tk.Button(result_frame, text="Retour au menu", command=lambda: go_menu(root), font=("Helvetica", 18))
    stop_button.pack(pady=5)

def go_menu(root):
    from menu_page import MenuPage
    print("Fin de la partie")
    root.destroy()  # Ferme la fenêtre du menu
    root = tk.Tk()
    menu = MenuPage(root) 
    root.mainloop()