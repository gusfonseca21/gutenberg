import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from core.file_manager import listar_arquivos
from core.printer import imprimir_arquivo

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gutenberg")
        self.geometry("500x400")

        # Botão para escolher diretório
        btn_dir = tk.Button(self, text="Escolher Diretório", command=self.selecionar_diretorio)
        btn_dir.pack(pady=10)

        # Lista de arquivos
        self.listbox = Listbox(self, width=60)
        self.listbox.pack(pady=10)

        # Botão para imprimir arquivo selecionado
        btn_print = tk.Button(self, text="Imprimir Selecionado", command=self.imprimir)
        btn_print.pack(pady=10)

    def selecionar_diretorio(self):
        caminho = filedialog.askdirectory()
        if not caminho:
            return

        arquivos = listar_arquivos(caminho)

        self.listbox.delete(0, tk.END)
        for arq in arquivos:
            self.listbox.insert(tk.END, arq)

    def imprimir(self):
        selecionado = self.listbox.get(tk.ACTIVE)
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um arquivo")
            return

        imprimir_arquivo(selecionado)
