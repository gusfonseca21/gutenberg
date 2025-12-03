import os
import sys

def resource_path(relative_path):
    """
    Retorna o caminho correto para um recurso,
    funcionando tanto no desenvolvimento quanto no executável PyInstaller.
    """
    if hasattr(sys, "_MEIPASS"):
        # Quando empacotado no .exe
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Quando rodando pelo Python normal
        return os.path.join(os.path.abspath("."), relative_path)