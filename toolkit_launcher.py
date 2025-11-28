import os
import importlib

TOOLS = {
    "1": ("Text Processor", "tools.text_processor"),
    "2": ("Memory Calculator", "tools.memory_calculator"),
    "3": ("CSV Tool", "tools.csv_tool"),
    "4": ("File Organizer", "tools.file_organizer"),
    "0": ("Exit", None)
}

def run_tool(module_path):
    module = importlib.import_module(module_path)
    if hasattr(module, "main"):
        module.main()
    else:
        print("⚠️ This tool has no main() function to run.")

def show_menu():
    print("\n=== Python Toolkit Launcher ===")
    for key, (name, _) in TOOLS.items():
        print(f"[{key}] {name}")
    print("==============================")

def main():
    while True:
        show_menu()
        choice = input("Select a tool: ").strip()

        if choice == "0":
            print("Exiting toolkit. Goodbye!")
            break

        if choice not in TOOLS:
            print("Invalid selection.")
            continue

        print(f"\nRunning: {TOOLS[choice][0]}...\n")
        run_tool(TOOLS[choice][1])

if __name__ == "__main__":
    main()