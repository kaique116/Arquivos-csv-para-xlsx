import tkinter as tk
from tkinter import messagebox
import pandas as pd

def transformar_arquivos_csv_para_excel():
    try:     
        arquivo_csv = pd.read_csv(colocar_arquivo.get())

        arquivo_xlsx = arquivo_csv.to_excel('arquivo_convertido.xlsx', index=False)
        
        messagebox.showinfo("Sucesso", "Arquivo CSV convertido para Excel com sucesso!")


    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter o arquivo: {str(e)}")

janela = tk.Tk()

janela.title("Conversor de arquivos CSV para xlsx")

janela.geometry("400x200")

colocar_arquivo = tk.Entry(janela, width=30)
colocar_arquivo.pack(pady=20)

botao = tk.Button(janela, text="Converter", command=transformar_arquivos_csv_para_excel)
botao.pack()

janela.mainloop()
