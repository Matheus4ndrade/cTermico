import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from excel_utils import save_to_excel

def create_modal_with_graph(root, data, title, xlabel, ylabel, unit):
    modal = tk.Toplevel(root)
    modal.title(title)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    modal.geometry(f"{screen_width}x{screen_height}")
    modal.configure(bg="#797979") 

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([d[0] for d in data], [d[1] for d in data], marker="o", label="Temperatura")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend()

    button_frame = tk.Frame(modal, bg="#797979") 
    button_frame.pack(pady=10)

    save_button = tk.Button(
        button_frame,
        text="Salvar em Excel",
        command=lambda: save_to_excel(data, title),
        bg="#008000",
        fg="white",  
        font=("Arial", 10, "bold"),
        relief="raised"
    )
    save_button.pack(side=tk.LEFT, padx=5)

    close_button = tk.Button(
        button_frame,
        text="Fechar",
        command=modal.destroy,
        bg="#FF0000",
        fg="white", 
        font=("Arial", 10, "bold"),
        relief="raised"
    )
    close_button.pack(side=tk.LEFT, padx=5)

    canvas = FigureCanvasTkAgg(fig, master=modal)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    text_area = tk.Text(
        modal,
        height=10,
        wrap=tk.WORD,
        font=("Courier", 12),
        bg="#797979",  
        fg="white" 
    )
    text_area.pack(fill=tk.BOTH, padx=10, pady=10)

    for x, y in data:
        formatted_x = f"{x:.1f}"
        text_area.insert(tk.END, f"{formatted_x} {unit}: {y}°C\n")
