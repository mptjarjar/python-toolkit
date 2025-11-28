import csv
import os

def read_csv(file_path):
    """Read and display CSV contents."""
    if not os.path.exists(file_path):
        print("⚠️ File not found.")
        return

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("\n📄 CSV Contents:")
        for row in reader:
            print(row)

def write_csv(file_path):
    """Add a new row to the CSV file."""
    new_row = input("Enter a new row (comma-separated): ").split(",")

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([value.strip() for value in new_row])

    print("✅ Row added successfully.")

def main():
    logs_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(logs_folder, exist_ok=True)

    file_path = input("Enter CSV file path (or press Enter to create example.csv): ").strip()

    if not file_path:
        file_path = os.path.join(logs_folder, "example.csv")

        # Create file if it doesn't exist yet
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["item", "price", "quantity"])

    print("\n1. Read CSV")
    print("2. Add Row")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        read_csv(file_path)
    elif choice == "2":
        write_csv(file_path)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
