import os
import shutil
from datetime import datetime

# Log any message to logs/organizer_log.txt
def log_action(message):
    log_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_folder, exist_ok=True)

    log_path = os.path.join(log_folder, "organizer_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")


def get_unique_filename(folder, filename):
    """Avoid overwriting files by adding _1, _2, _3..."""
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name


def organize_files(source_folder):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".txt", ".pdf", ".docx"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov"],
        "Archives": [".zip", ".tar", ".gz"],
        "Python": [".py"]
    }

    # Create destination folders
    for folder in file_types.keys():
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

    for filename in os.listdir(source_folder):
        # Skip hidden files
        if filename.startswith('.'):
            continue
        
        filepath = os.path.join(source_folder, filename)

        # Skip directories or the script itself
        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                destination_folder = os.path.join(source_folder, folder)

                unique_name = get_unique_filename(destination_folder, filename)
                shutil.move(filepath, os.path.join(destination_folder, unique_name))

                print(f"📁 Moved: {filename} → {folder}/{unique_name}")
                log_action(f"Moved '{filename}' to '{folder}/{unique_name}'")

                moved = True
                break

        if not moved:
            print(f"⚠️ Skipped: {filename} (unknown type)")
            log_action(f"Skipped unknown file: {filename}")


if __name__ == "__main__":
    target = input("Enter folder path to organize (press Enter for current folder): ").strip()
    if not target:
        target = os.getcwd()

    print(f"Organizing: {target}")
    organize_files(target)
    print("✅ Organization complete.")