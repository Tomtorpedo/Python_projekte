import tkinter as tk
from tkinter import ttk

def close_app():
    app.destroy()

def start_update():
    # Entferne die Buttons
    yes_button.pack_forget()
    no_button.pack_forget()
    question_label.config(text="")

    # Ladebalken anzeigen
    progress.pack(pady=20)
    status_label.pack()
    app.after(100, download_phase)

def download_phase():
    status_label.config(text="lade virus.exe herunter...")
    progress['value'] = 33
    app.after(2000, install_phase)

def install_phase():
    status_label.config(text="installiere virus.exe...")
    progress['value'] = 66
    app.after(2000, finish_phase)

def finish_phase():
    status_label.config(text="internet ist neu geupdated.")
    progress['value'] = 100

app = tk.Tk()
app.title("Internet Update")

question_label = tk.Label(app, text="möchte er den Internet updaten?", font=("Arial", 14))
question_label.pack(pady=20)

yes_button = tk.Button(app, text="Да", width=10, command=start_update)
yes_button.pack(side="left", padx=30, pady=10)

no_button = tk.Button(app, text="нет", width=10, command=close_app)
no_button.pack(side="right", padx=30, pady=10)

progress = ttk.Progressbar(app, orient="horizontal", length=300, mode="determinate")
status_label = tk.Label(app, text="", font=("Arial", 12))

app.mainloop()