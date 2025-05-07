import tkinter as tk
from gf_gen import gf_gen

def show_result():
    mutter_nat, vater_nat = gf_gen()
    result = f"Jans Freundin ist halb {mutter_nat}, halb {vater_nat}."
    result_label.config(text=result)

app = tk.Tk()
app.title("Jans Freundin Generator")

generate_button = tk.Button(app, text="Generiere Jans Freundin", command=show_result)
generate_button.pack(pady=20)

result_label = tk.Label(app, text="", wraplength=300)
result_label.pack(pady=20)

app.mainloop()