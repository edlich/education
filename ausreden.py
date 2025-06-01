import tkinter as tk
from tkinter import ttk  # ttk für modernere Widgets
import random

# --- Die Logik für die Ausrede bleibt gleich ---
def generiere_ausrede():
    anfang = [
        "Ich konnte leider nicht, weil",
        "Es ging leider nicht, da",
        "Leider musste ich passen, denn",
        "Du glaubst es nicht, aber",
        "Mein Hund hat meine Ausrede gefressen, aber",
        "Ich war kurz davor, als"
    ]

    adjektiv = [
        "ein außerirdisches",
        "ein fliegendes",
        "ein winziges",
        "ein riesiges",
        "ein stinkendes",
        "ein singendes"
    ]

    nomen = [
        "Einhorn",
        "Raumschiff",
        "Erdmännchen",
        "Nilpferd",
        "Gummibärchen",
        "U-Boot"
    ]

    ende = [
        "meinen Hausschuh entführt hat.",
        "eine Teeparty veranstaltet hat.",
        "angefangen hat, Opern zu singen.",
        "das Universum retten musste.",
        "sich in eine Pizza verwandelt hat.",
        "mich zum Tanz aufgefordert hat."
    ]

    ausrede = random.choice(anfang) + " " + \
              random.choice(adjektiv) + " " + \
              random.choice(nomen) + " " + \
              random.choice(ende)
    return ausrede

# --- GUI-Teil ---
def aktualisiere_ausrede():
    """Generiert eine neue Ausrede und aktualisiert das Label."""
    neue_ausrede = generiere_ausrede()
    ausrede_label.config(text=f"„{neue_ausrede}“") # Aktualisiert den Text des Labels

# Hauptfenster erstellen
root = tk.Tk()
root.title("Zufalls-Ausreden-Generator")
root.geometry("600x250") # Breite x Höhe
root.resizable(False, False) # Fenstergröße nicht änderbar

# Styling (optional, für ein moderneres Aussehen)
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 14), foreground="#333333", wraplength=550) # wraplength für Zeilenumbruch

# Willkommensnachricht
willkommen_label = ttk.Label(root, text="Klicke auf den Knopf für deine nächste geniale Ausrede!", font=("Arial", 14, "bold"))
willkommen_label.pack(pady=20) # Fügt oben etwas Abstand hinzu

# Label für die Ausrede
# Ein leeres Label, das später mit der Ausrede gefüllt wird
ausrede_label = ttk.Label(root, text="Hier erscheint deine Ausrede...", anchor="center")
ausrede_label.pack(pady=10)

# Button zum Generieren der Ausrede
# Der command-Parameter sagt, welche Funktion beim Klick ausgeführt werden soll
generieren_button = ttk.Button(root, text="Neue Ausrede!", command=aktualisiere_ausrede)
generieren_button.pack(pady=20) # Fügt unten etwas Abstand hinzu

# GUI starten
root.mainloop()