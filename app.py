import tkinter as tk
from tkinter import ttk, messagebox
from calculations import calculate_equation
from modals import create_modal_with_graph
from about_modal import show_about_author 

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ciclo Térmico")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.inputs = {}
        self.input_widgets = {}
        self.style = ttk.Style()
        self.style.configure("TEntry", background="#797979")
        self.style.configure("TButton", background="#008000", foreground="white", font=("Arial", 10, "bold"))
        self.style.configure("TLabel", background="#797979", foreground="white", font=("Arial", 10))

        self.create_input_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_input_screen(self):
        self.clear_screen()

        header_frame = tk.Frame(self.root, bg="#4f4f4f", height=50)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(
            header_frame, text="Ciclo Térmico", bg="#4f4f4f", fg="white", font=("Arial", 24, "bold")
        )
        header_label.pack(pady=10)
        about_button = tk.Button(
            header_frame,
            text="Sobre o Autor",
            command=lambda: show_about_author(self.root),
            bg="#007BFF",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
        )
        about_button.place(relx=0.95, rely=0.5, anchor="e")
        separator = tk.Frame(self.root, bg="white", height=1)
        separator.pack(fill=tk.X)
        container_frame = tk.Frame(self.root, bg="#797979")
        container_frame.pack(fill=tk.BOTH, expand=True)
        blue_container = tk.Frame(container_frame, bg="#797979", width=400, height=600)
        blue_container.place(relx=0.5, y=5, anchor="n")
        blue_container.pack_propagate(False)

        inputs = [
            ("Temperatura de Pico (°C)", "tp"),
            ("Temperatura Inicial (°C)", "to"),
            ("Tensão (V)", "tensao"),
            ("Amperagem (I)", "amperagem"),
            ("Velocidade de Soldagem (mm/min)", "velocidadeSoldagem"),
            ("Valor de n", "n"),
            ("Densidade do Material (Kg/m³)", "densidade"),
            ("Calor Específico (Cp)", "calorEspecifico"),
            ("Espessura da Chapa (mm)", "espessuraChapa"),
            ("Número de Escalas (mm)", "distancia"),
            ("Temperatura de Fusão do Material (°C)", "temperaturaFusao"),
        ]
        self.input_widgets = {}

        for label_text, key in inputs:
            label = ttk.Label(blue_container, text=label_text, style="TLabel", background="#797979", foreground="white")
            label.pack(pady=2, anchor="w", padx=5)
            entry = ttk.Entry(blue_container)
            entry.pack(pady=2, padx=5, fill=tk.X)
            self.input_widgets[key] = entry

        calculate_button = tk.Button(
            blue_container,
            text="Calcular",
            command=self.calculate,
            bg="#008000",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
        )
        calculate_button.pack(pady=10)

    def calculate(self):
        inputs = {
            key: self.parse_float(entry.get()) for key, entry in self.input_widgets.items()
        }
        if None in inputs.values():
            messagebox.showerror("Erro", "Por favor, insira todos os valores corretamente.")
            return
        if inputs.get("distancia", 0) > 20:
            messagebox.showerror("Erro", "O valor máximo para Número de Escalas é 20.")
            return
        try:
            results = calculate_equation(inputs)
            self.show_results(results)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular os resultados: {e}")

    def parse_float(self, value):
        try:
            value = value.replace(",", ".")
            return round(float(value), 2)
        except ValueError:
            return None
    def show_results(self, results):
        self.clear_screen()
        results_frame = tk.Frame(self.root, bg="#797979")
        results_frame.pack(fill=tk.BOTH, expand=True)
        back_button = tk.Button(
            results_frame,
            text="← Voltar",
            command=self.create_input_screen,
            bg="#FF0000", 
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
        )
        back_button.pack(pady=10, anchor="w", padx=10)

        tk.Label(
            results_frame,
            text="Resultados",
            font=("Arial", 16, "bold"),
            bg="#797979",
            fg="white",
        ).pack(pady=10)

        for key, value in results.items():
            if key not in ["data_distancia", "data_tempo"]:
                tk.Label(
                    results_frame, text=f"{key}: {value}", bg="#797979", fg="white"
                ).pack(pady=5)

        button_frame = tk.Frame(results_frame, bg="#797979")
        button_frame.pack(pady=10)

        button_temp_dist = tk.Button(
            button_frame,
            text="Mostrar Temperatura x Distância",
            command=lambda: self.show_graph("Distância", results["data_distancia"], "mm"),
            bg="#008000",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
        )
        button_temp_dist.pack(side=tk.LEFT, padx=5)

        button_temp_time = tk.Button(
            button_frame,
            text="Mostrar Temperatura x Tempo",
            command=lambda: self.show_graph("Tempo", results["data_tempo"], "s"),
            bg="#008000",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
        )
        button_temp_time.pack(side=tk.LEFT, padx=5)

    def show_graph(self, graph_type, data, unit):
        title = f"Temperatura x {graph_type}"
        xlabel = f"{graph_type} ({unit})"
        ylabel = "Temperatura (°C)"
        create_modal_with_graph(self.root, data, title, xlabel, ylabel, unit) 