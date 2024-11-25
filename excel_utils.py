import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import tempfile
from openpyxl.utils.dataframe import dataframe_to_rows 

def save_to_excel(data, title):
    df = pd.DataFrame(data, columns=["X", "Temperatura (°C)"])
    file_path = asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Arquivos Excel", "*.xlsx"), ("Todos os Arquivos", "*.*")],
        title=f"Salvar {title}",
    )

    if file_path:
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot([d[0] for d in data], [d[1] for d in data], marker="o", label="Temperatura")
            ax.set_title(title)
            ax.set_xlabel("Distância (mm)") 
            ax.set_ylabel("Temperatura (°C)")
            ax.grid(True)
            ax.legend()

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
                tmpfile_path = tmpfile.name
                fig.savefig(tmpfile_path)
                plt.close(fig) 
            wb = Workbook()
            ws = wb.active
            ws.title = title
            for row in dataframe_to_rows(df, index=False, header=True):
                ws.append(row)
                img = Image(tmpfile_path)
                ws.add_image(img, "E5")  
                wb.save(file_path)

            messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{e}")
