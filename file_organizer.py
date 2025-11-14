import os
import shutil
from datetime import datetime

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "audio": [".mp3", ".wav", ".flac"],
    "videos": [".mp4", ".mov", ".avi"],
    "archives": [".zip", ".tar", ".gz"],
    "code": [".py", ".js", ".html", ".css"]
}

def log_action(message, logfile):
    with open(logfile, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def ensure_unique_name(destination_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    # If the file already exists, generate a new name
    while os.path.exists(os.path.join(destination_folder, new_name)):
        new_name = f"{base}({counter}){ext}"
        counter += 1

    return new_name

def organize_files(source_folder):
    log_file = os.path.join(source_folder, "organizer_log.txt")

    # Create subfolders
    for folder in file_types:
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

    # Iterate through folder
    for filename in os.listdir(source_folder):
        # Skip hidden files (starting with .)
        if filename.startswith("."):
            continue

        filepath = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Skip the script itself
        if filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                destination = os.path.join(source_folder, folder)

                # Avoid overwriting by ensuring a unique name
                safe_name = ensure_unique_name(destination, filename)

                shutil.move(filepath, os.path.join(destination, safe_name))

                print(f"📁 Moved: {filename} → {folder}/{safe_name}")
                log_action(f"Moved: {filename} → {folder}/{safe_name}", log_file)

                moved = True
                break

        if not moved:
            print(f"⚠️ Skipped: {filename} (unknown type)")
            log_action(f"Skipped: {filename} (unknown type)", log_file)

if __name__ == "__main__":
    target = input("Enter the folder path to organize (press Enter for current folder): ").strip()
    if not target:
        target = os.getcwd()

    print(f"Organizing files in: {target}")
    organize_files(target)
    print("✅ Organization complete!")
