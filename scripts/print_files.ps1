param(
    [string]$FilePaths
)

$files = $FilePaths -split ";"

foreach ($file in $files) {
    Write-Host "Imprimindo: $file"
    Start-Process -FilePath $file -Verb Print
    Start-Sleep -Milliseconds 500
}