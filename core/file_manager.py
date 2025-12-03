import os

def list_files(diretorio):
    """
    Lista recursivamente todos os arquivos de documentos com extensões comuns 
    de impressão dentro do diretório especificado.
    """
    # Extensões comuns para documentos de impressão
    EXTENSOES_IMPRESSAO = (
        '.pdf',     # Portable Document Format (Mais comum para impressão)
        '.docx',    # Microsoft Word Document
        '.doc',     # Antigo Microsoft Word Document
        '.xlsx',    # Microsoft Excel Spreadsheet
        '.xls',     # Antigo Microsoft Excel Spreadsheet
        '.pptx',    # Microsoft PowerPoint Presentation
        '.txt',     # Texto Simples
        '.jpg',     # Imagens (frequentemente impressas)
        '.png',     # Imagens (frequentemente impressas)
    )
    
    documentos = []
    
    # Se o diretório não existir, retorne vazio
    if not os.path.isdir(diretorio):
        print(f"Erro: O diretório '{diretorio}' não foi encontrado.")
        return documentos

    # Percorre os arquivos no diretório
    for nome in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, nome)
        
        # 1. Verifica se é um arquivo (não pasta)
        if os.path.isfile(caminho_completo):
            # 2. Verifica a extensão do arquivo em minúsculas
            extensao = os.path.splitext(nome)[1].lower()
            
            if extensao in EXTENSOES_IMPRESSAO:
                documentos.append(caminho_completo)
                
    return documentos