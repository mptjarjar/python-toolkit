import os

tools = {
    "1": ("Text Processor", "text_processor.py"),
    "2": ("File Organizer", "file_organizer.py"),
    "3": ("Memory Calculator", "memory_calculator.py")
}

def run_tool(script):
    os.system(f"python3 {script}")

def main():
    while True:
        print("\n=== PYTHON TOOLKIT MENU ===")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")
        print("0. Exit")
        
        choice = input("Choose a tool (number): ").strip()
        
        if choice == "0":
            print("Goodbye!")
            break
        
        if choice in tools:
            print(f"Running: {tools[choice][0]}...\n")
            run_tool(tools[choice][1])
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()