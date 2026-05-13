import tkinter as tk
from tkinter import messagebox
import pandas as pd
import time



def transformar_arquivos_csv_para_excel():
    try:     
        arquivo_csv = pd.read_csv(colocar_arquivo.get())

        arquivo_xlsx = arquivo_csv.to_excel('arquivo_convertido.xlsx', index=False)
        
        messagebox.showinfo("Sucesso", "Arquivo CSV convertido para Excel com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter o arquivo: {str(e)}")

def salvar_informacoes():
    try:
        with open("informacoes.txt", "a") as arquivo:
            arquivo.write(f"Arquivo convertido: {colocar_arquivo.get()} - Data e hora: {time.ctime()}\n")
            messagebox.showinfo("Sucesso", "Informações salvas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar as informações: {str(e)}")

def combinar_funcoes():
    transformar_arquivos_csv_para_excel()
    salvar_informacoes()

janela = tk.Tk()

janela.title("Conversor de arquivos CSV para xlsx")

janela.geometry("400x200")

colocar_arquivo = tk.Entry(janela, width=30)
colocar_arquivo.pack(pady=20)

botao = tk.Button(janela, text="Converter", command=combinar_funcoes)
botao.pack()


janela.mainloop()
