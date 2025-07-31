import argparse
import os
import shutil
import kagglehub

def download_dataset(output_artifact):
    # Dataset von KaggleHub laden
    print("🔄 Lade Dataset herunter...")
    path = kagglehub.dataset_download("wasiqaliyasir/breast-cancer-dataset")
    print(f"📥 Heruntergeladen nach: {path}")

    # Zielordner erstellen
    os.makedirs(output_artifact, exist_ok=True)

    # Dateien aus dem KaggleHub-Verzeichnis ins output_artifact kopieren
    for file in os.listdir(path):
        src = os.path.join(path, file)
        dst = os.path.join(output_artifact, file)
        shutil.copy2(src, dst)

    print(f"✅ Dataset gespeichert unter: {output_artifact}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download dataset from KaggleHub.")
    parser.add_argument("--output_artifact", type=str, required=True, help="Pfad zum Zielordner für das Dataset")
    args = parser.parse_args()

    download_dataset(args.output_artifact)
