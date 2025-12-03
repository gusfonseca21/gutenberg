import subprocess
import os
from core.utils import resource_path


def get_selected_printer():
    ps1_path = resource_path("scripts/get_selected_printer.ps1")

    result = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", ps1_path
        ],
        capture_output=True,
        text=True,
        check=False
    )

    printer_name = result.stdout.strip()

    # Impressoras PDF geralmente não são válidas
    is_valid = "pdf" not in printer_name.lower()

    return {
        "name": printer_name,
        "is_valid": is_valid
    }


def print_files(file_paths_list):
    normalized = [os.path.normpath(p) for p in file_paths_list]
    joined = ";".join(normalized)

    ps1_path = resource_path("scripts/print_files.ps1")

    result = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", ps1_path,
            "-FilePaths", joined
        ],
        capture_output=True,
        text=True,
        check=False
    )

    error_message = result.stderr.strip()

    if result.returncode != 0:
        print(error_message)
        raise RuntimeError(
            f"Falha na impressão via PowerShell. Detalhes: {error_message}"
        )

    if error_message:
        print(f"AVISO POWERSHELL: {error_message}")
        raise RuntimeError(
            f"Aviso na execução do PowerShell. Detalhes: {error_message}"
        )


def open_print_queue():
    ps1_path = resource_path("scripts/open_print_queue.ps1")

    subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", ps1_path
        ],
        capture_output=True,
        text=True
    )
