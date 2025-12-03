
$PrinterString = (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Windows').Device

# 2. Extrai apenas o nome da impressora (o primeiro elemento antes da vírgula)
$DefaultPrinterName = $PrinterString.Split(',')[0]

# 3. Verifica se o nome foi obtido
if ($DefaultPrinterName) {
    Write-Host "Abrindo fila de impressão para: $DefaultPrinterName"
    
    # 💥 CORREÇÃO PARA EVITAR TRAVAMENTO (ASSÍNCRONA) 💥
    # Usamos Start-Process para que o comando RUNDLL32 execute em segundo plano,
    # permitindo que o script PowerShell termine imediatamente.
    $Arguments = "PRINTUI.DLL,PrintUIEntry /o /n `"$DefaultPrinterName`""
    Start-Process -FilePath "RUNDLL32" -ArgumentList $Arguments -NoNewWindow -Wait:$false
} else {
    Write-Warning "Não foi possível determinar a impressora padrão."
}

# O script sai com sucesso (código 0) imediatamente após iniciar a fila de impressão.
exit 0