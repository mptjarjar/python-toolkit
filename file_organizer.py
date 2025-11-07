import os
import shutil

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

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(source_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Go through files and move them
    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)

        # Skip folders and the script itself
        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(filepath, os.path.join(source_folder, folder, filename))
                print(f"📁 Moved: {filename} → {folder}/")
                moved = True
                break

        if not moved:
            print(f"⚠️ Skipped: {filename} (unknown type)")

if __name__ == "__main__":
    target = input("Enter the folder path to organize (press Enter for current folder): ").strip()
    if not target:
        target = os.getcwd()
    
    print(f"Organizing files in: {target}")
    organize_files(target)
    print("✅ Organization complete!")