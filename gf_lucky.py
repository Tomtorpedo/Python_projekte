import tkinter as tk
import random
import time
from gf_gen import gf_gen

# Liste von Beispiel-Nationalitäten für die Animation
nationalities = gf_gen(T=1)

def spin_labels():
    """Simuliert das Rotieren der Nationalitäten wie in einem Spielautomaten."""
    for _ in range(20):  # Anzahl der Rotationen
        random_mutter = random.choice(nationalities)
        random_vater = random.choice(nationalities)
        result_label.config(text=f"Jans Freundin ist halb {random_mutter}, halb {random_vater}.")
        app.update()  # Aktualisiert die GUI
        time.sleep(0.1)  # Kurze Pause für den Animationseffekt

def show_result():
    """Zeigt das endgültige Ergebnis nach der Animation."""
    spin_labels()  # Animation starten
    mutter_nat, vater_nat = gf_gen()  # Endgültige Nationalitäten generieren
    result = f"Jans Freundin ist halb {mutter_nat}, halb {vater_nat}."
    result_label.config(text=result)

app = tk.Tk()
app.title("Jans Freundin Generator")

generate_button = tk.Button(app, text="Generiere Jans Freundin", command=show_result)
generate_button.pack(pady=20)

result_label = tk.Label(app, text="Drücke den Knopf, um zu starten!", wraplength=300, font=("Helvetica", 14))
result_label.pack(pady=20)

app.mainloop()