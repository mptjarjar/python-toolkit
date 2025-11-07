# file_organizer.py
import os
import shutil
from datetime import datetime

def log_action(message, logfile="organizer_log.txt"):
    """Append a message to the log file with timestamp."""
    with open(logfile, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def organize_files(source_folder):
    """Organize files in the source folder by type."""
    file_types = {
        "Documents": [".pdf", ".docx", ".txt", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".tar", ".gz"],
        "Python": [".py"],
    }

    for folder in file_types.keys():
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)

        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(filepath, os.path.join(source_folder, folder, filename))
                print(f"📁 Moved: {filename} → {folder}/")
                log_action(f"Moved: {filename} → {folder}/")
                moved = True
                break

        if not moved:
            print(f"⚠️ Skipped: {filename} (unknown type)")
            log_action(f"Skipped: {filename} (unknown type)")

if __name__ == "__main__":
    target = input("Enter the folder path to organize (press Enter for current folder): ").strip()
    if not target:
        target = os.getcwd()
    
    print(f"Organizing files in: {target}")
    log_action(f"Started organizing folder: {target}")
    organize_files(target)
    log_action("✅ Organization complete\n")
    print("✅ Organization complete!")