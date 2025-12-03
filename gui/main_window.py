import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from tkinter import font as tkfont
from core.file_manager import list_files
from core.printer import get_selected_printer, print_files, open_print_queue
import random

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        window_width = 500
        window_height = 500

        self.title("Gutenberg")
        self.geometry(f"{str(window_width)}x{str(window_height)}")
        self.center_window(window_width, window_height)

        # Variáveis de instância para referenciar os widgets e configurações
        self.printer_font = tkfont.Font(family="Arial", size=14, weight="bold")
        self.selected_printer_name_label = None
        self.current_printer_data = {}

        tk.Label(self, text="Impressora Selecionada:", anchor="w").pack(
            side="top", fill="x", padx=10, pady=(10, 0)
        )

        printer_line_frame = tk.Frame(self)
        printer_line_frame.pack(side="top", fill="x", padx=10, pady=5)

        self.setup_printer_widgets(printer_line_frame)
        self.update_printer_display()

        # Botão para escolher diretório
        btn_dir = tk.Button(self, text="Escolher Diretório", command=self.select_dir)
        btn_dir.pack(pady=10)
        
        # Lista de arquivos
        self.listbox = Listbox(self, width=window_width)
        self.listbox.pack(pady=10)

        self.lbl_total = tk.Label(self, text="Total de arquivos: 0")
        self.lbl_total.pack(pady=5)

        # Botão para imprimir arquivo selecionado
        self.btn_print = tk.Button(self, text="Imprimir Arquivos", command=self.imprimir)
        self.btn_print.pack(pady=10)
        self.btn_print.config(state="disabled")


    def select_dir(self):
        caminho = filedialog.askdirectory()
        if not caminho:
            return

        files = list_files(caminho)

        self.listbox.delete(0, tk.END)
        for file in files:
            self.listbox.insert(tk.END, file)
        
        self.lbl_total.config(text=f"Total de arquivos: {len(files)}")
        
        self.btn_print.config(state="normal")

    def imprimir(self):
            selected_files = self.listbox.get(0, tk.END)
            if not selected_files:
                messagebox.showwarning("Aviso", "Selecione um arquivo")
                return

            try:
                # Tenta enviar os arquivos para impressão via função externa
                print_files(selected_files)
                open_print_queue()
                self.btn_print.config(state="disabled")
                

            except RuntimeError as e:
                # Captura o erro específico que print_files levanta (contém a mensagem do PowerShell)
                # Converte a exceção 'e' para string para obter a mensagem
                messagebox.showerror("Erro de Impressão", str(e))
            
            except Exception as e:
                # Captura outros erros inesperados que podem ocorrer no subprocesso
                messagebox.showerror("Erro Inesperado", f"Ocorreu um erro ao processar: {e}")

    def setup_printer_widgets(self, parent_frame):
            """Cria o Label do nome da impressora e o Botão dentro do Frame."""

            # Label para o nome da impressora (colocado na esquerda do Frame)
            # O texto inicial pode ser vazio, será preenchido por update_printer_display()
            self.selected_printer_name_label = tk.Label(
                parent_frame, 
                text="Carregando...", 
                anchor="w", 
                font=self.printer_font,
                fg="darkblue"
            )
            self.selected_printer_name_label.pack(side="left", fill="x", expand=True)

            # Botão de Atualização (colocado na direita do Frame)
            # O comando chama a função que faz a busca e a atualização
            update_button = tk.Button(
                parent_frame, 
                text="Atualizar", 
                command=self.update_printer_display,
                relief="groove"
            )
            update_button.pack(side="right", padx=(10, 0))    

    def update_printer_display(self):
        """Busca o novo valor, atualiza a variável e o texto do Label."""
        
        # 1. Atualiza a variável de instância com o novo dicionário
        self.current_printer_data = get_selected_printer()
        
        # 2. Prepara o novo texto
        printer_data = self.current_printer_data
        
        # Usa a sintaxe ternária correta de Python
        status_text = "" if printer_data.get("is_valid", False) else "(INVÁLIDA)"
        
        # Cria a string final que será exibida
        new_text = f"{printer_data['name']} {status_text}"
        
        # 3. Atualiza o texto do Label existente
        self.selected_printer_name_label.config(text=new_text) # type: ignore

    def center_window(self, window_width, window_height):
        self.update_idletasks()

        # Dimensões do monitor
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular a posição central
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Setando a posição da janela
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")