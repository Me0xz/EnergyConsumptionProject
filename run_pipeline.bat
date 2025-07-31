@echo off
SET ENV_NAME=get_data_env

REM === Schritt 1: Environment erstellen, wenn nötig ===
CALL conda env list | findstr %ENV_NAME%
IF %ERRORLEVEL% NEQ 0 (
    echo 📦 Erstelle Conda-Umgebung %ENV_NAME% ...
    CALL conda env create -f environment\conda.yml
)

REM === Schritt 2: Umgebung aktivieren ===
CALL conda activate %ENV_NAME%

REM === Schritt 3: Pipeline-Schritte ausführen ===
echo 🚀 Starte Daten-Download...
python src\get_data\get_data.py --output_artifact data\raw

REM Optional:
REM echo 🔧 Starte Datenbereinigung...
REM python src\clean_data\clean_data.py --input_artifact data\raw --output_artifact data\clean

echo ✅ Pipeline abgeschlossen.
pause
