import tkinter as tk
from tkinter import Toplevel
import webbrowser

def show_about_author(parent):
    about_window = Toplevel(parent)
    about_window.title("Sobre o Autor")
    about_window.geometry("400x300")
    about_window.configure(bg="#797979")
    about_window.transient(parent)
    about_window.grab_set()

    tk.Label(
        about_window,
        text="Sobre o Autor",
        font=("Arial", 16, "bold"),
        bg="#797979",
        fg="white",
    ).pack(pady=10)

    tk.Label(
        about_window,
        text="Este aplicativo foi desenvolvido como \n"
        "parte de um TG para a análise de ciclos \n"
        "térmicos para melhorias de implementação,\n"
        "ou entrar em contato segue os links abaixo \n"
        "para mais:\n",
        font=("Arial", 12),
        bg="#797979",
        fg="white",
        justify="center",
    ).pack(pady=10)

    tk.Button(
        about_window,
        text="LinkedIn",
        command=lambda: webbrowser.open("https://www.linkedin.com/in/matheus-andrade-4449212b7/"),
        bg="#007BFF",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(pady=5)

    tk.Button(
        about_window,
        text="GitHub",
        command=lambda: webbrowser.open("https://github.com/Matheus4ndrade"),
        bg="#007BFF",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(pady=5)

    tk.Button(
        about_window,
        text="Fechar",
        command=about_window.destroy,
        bg="#FF0000",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(pady=10)
