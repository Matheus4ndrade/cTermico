import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import tempfile
from openpyxl.utils.dataframe import dataframe_to_rows  # Adicionado o import

def save_to_excel(data, title):
    """Salva os dados do gráfico e o gráfico em si em um arquivo Excel."""
    # Cria um DataFrame com os dados
    df = pd.DataFrame(data, columns=["X", "Temperatura (°C)"])

    # Solicita o caminho para salvar o arquivo
    file_path = asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Arquivos Excel", "*.xlsx"), ("Todos os Arquivos", "*.*")],
        title=f"Salvar {title}",
    )

    if file_path:
        try:
            # Cria o gráfico
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot([d[0] for d in data], [d[1] for d in data], marker="o", label="Temperatura")
            ax.set_title(title)
            ax.set_xlabel("Distância (mm)")  # Ou outro rótulo adequado
            ax.set_ylabel("Temperatura (°C)")
            ax.grid(True)
            ax.legend()

            # Salva o gráfico em um arquivo temporário PNG
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
                tmpfile_path = tmpfile.name
                fig.savefig(tmpfile_path)
                plt.close(fig)  # Fecha o gráfico após salvar

            # Cria um novo workbook e adiciona os dados ao Excel
            wb = Workbook()
            ws = wb.active
            ws.title = title
            for row in dataframe_to_rows(df, index=False, header=True):
                ws.append(row)

            # Adiciona a imagem ao Excel
            img = Image(tmpfile_path)
            ws.add_image(img, "E5")  # Adiciona a imagem na célula E5 (ajuste conforme necessário)

            # Salva o arquivo Excel
            wb.save(file_path)

            messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{e}")
