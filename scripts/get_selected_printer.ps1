# Conteúdo de scripts/get_selected_printer.ps1
# ----------------------------------------------------------------------------------

# Usa o método do Registro que funcionou de forma confiável para obter o nome da impressora
$PrinterString = (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Windows').Device

# Divide a string pela vírgula e pega o primeiro elemento (o nome da impressora)
$PrinterName = $PrinterString.Split(',')[0]

# O cmdlet Write-Host deve ser EVITADO, pois envia para o host e não para a saída padrão (stdout)
# O comando abaixo escreve a variável diretamente no stdout para o Python capturar
Write-Output $PrinterName

# ----------------------------------------------------------------------------------