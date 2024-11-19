import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from excel_utils import save_to_excel  # Importando a função para salvar Excel

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("cTermico - Parâmetros de Entrada")
        self.root.geometry("600x600")
        self.inputs = {}
        self.input_widgets = {}
        self.create_input_screen()

    def clear_screen(self):
        """Remove todos os widgets da tela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_input_screen(self):
        """Cria a tela para inserção dos valores."""
        self.clear_screen()

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
            label = ttk.Label(self.root, text=label_text)
            label.pack(pady=2)
            entry = ttk.Entry(self.root)
            entry.pack(pady=2)
            self.input_widgets[key] = entry

        calculate_button = ttk.Button(
            self.root, text="Calcular", command=self.calculate_equation
        )
        calculate_button.pack(pady=20)

    def calculate_equation(self):
        """Calcula os valores de Heat Input e Resultado de Adams."""
        self.inputs = {
            key: self.parse_float(entry.get()) for key, entry in self.input_widgets.items()
        }

        if None in self.inputs.values():
            messagebox.showerror(
                "Erro", "Por favor, insira todos os valores corretamente."
            )
            return

        try:
            I = self.inputs["amperagem"]
            V = self.inputs["tensao"]
            n = self.inputs["n"]
            velocidadeSoldagem = self.inputs["velocidadeSoldagem"]
            Tp = self.inputs["tp"]
            To = self.inputs["to"]
            p = self.inputs["densidade"]
            Cp = self.inputs["calorEspecifico"]
            t = self.inputs["espessuraChapa"]
            Tm = self.inputs["temperaturaFusao"]

            Ht = (I * V * n * 60) / velocidadeSoldagem
            resulUm = 1 / (Tp - To)
            resulDois = (4.13 * ((p * Cp) / 1_000_000_000) * t) / Ht
            resulTres = 1 / (Tm - To)
            self.resultadoAdams = (resulUm - resulTres) / resulDois
            self.Ht = int(Ht)
            self.resulTres = resulTres
            self.To = To
            self.d = int(self.inputs["distancia"])
            self.velocidadeSoldagem = velocidadeSoldagem
            self.p = p
            self.Cp = Cp
            self.t = t
            self.show_results(self.Ht, round(self.resultadoAdams, 2))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular os resultados: {e}")

    def parse_float(self, value):
        """Converte um valor para float, aceitando vírgulas e pontos como separadores decimais."""
        try:
            value = value.replace(",", ".")
            return round(float(value), 2)
        except ValueError:
            return None

    def show_results(self, Ht, resultadoAdams):
        """Exibe os valores calculados na tela e adiciona o botão de voltar."""
        self.clear_screen()

        back_button = ttk.Button(self.root, text="← Voltar", command=self.create_input_screen)
        back_button.pack(pady=10, anchor="w")

        ttk.Label(self.root, text="Resultados", font=("Arial", 16, "bold")).pack(pady=10)

        ttk.Label(self.root, text=f"Heat Input (Ht): {Ht} J/mm").pack(pady=5)
        ttk.Label(self.root, text=f"Resultado de Adams: {resultadoAdams:.2f}").pack(pady=5)

        button_temp_dist = ttk.Button(self.root, text="Mostrar Temperatura x Distância", command=self.show_temperature_distance)
        button_temp_dist.pack(pady=10)

        button_temp_time = ttk.Button(self.root, text="Mostrar Temperatura x Tempo", command=self.show_temperature_time)
        button_temp_time.pack(pady=10)

    def create_modal_with_graph(self, data, title, xlabel, ylabel, unit):
        """Cria uma janela modal para exibir o gráfico e os dados."""
        modal = tk.Toplevel(self.root)
        modal.title(title)
        modal.geometry("800x600")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot([d[0] for d in data], [d[1] for d in data], marker="o", label="Temperatura")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True)
        ax.legend()

        save_button = ttk.Button(
            modal,
            text="Salvar em Excel",
            command=lambda: save_to_excel(data, title),
        )
        save_button.pack(pady=5)

        close_button = ttk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

        canvas = FigureCanvasTkAgg(fig, master=modal)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        text_area = tk.Text(modal, height=10, wrap=tk.WORD, font=("Courier", 12))
        text_area.pack(fill=tk.BOTH, padx=10, pady=10)
        for x, y in data:
            text_area.insert(tk.END, f"{x} {unit}: {y}°C\n")

        # Botão para salvar em Excel


    def show_temperature_distance(self):
        """Mostra o gráfico e os dados de Temperatura x Distância."""
        ciclos = [
            (i, round(1 / (((4.13 * ((self.p * self.Cp) / 1_000_000_000) * self.t * i) / self.Ht) + self.resulTres) + self.To))
            for i in range(self.d + 1)
        ]
        self.create_modal_with_graph(ciclos, "Temperatura x Distância", "Distância (mm)", "Temperatura (°C)", "mm")

    def show_temperature_time(self):
        """Mostra o gráfico e os dados de Temperatura x Tempo.""" 
        ciclos = [
            (i, round(1 / (((4.13 * ((self.p * self.Cp) / 1_000_000_000) * self.t * i) / self.Ht) + self.resulTres) + self.To))
            for i in range(self.d + 1)
        ]
        temperatura_tempo = [
            ((60 / self.velocidadeSoldagem) * ciclo[0], ciclo[1]) for ciclo in ciclos
        ]
        self.create_modal_with_graph(temperatura_tempo, "Temperatura x Tempo", "Tempo (s)", "Temperatura (°C)", "s")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
