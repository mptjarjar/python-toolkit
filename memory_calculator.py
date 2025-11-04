# memory_calculator.py

def calculate(memory, operation, number):
    """Perform basic math operations."""
    if operation == '+':
        return memory + number
    elif operation == '-':
        return memory - number
    elif operation == '*':
        return memory * number
    elif operation == '/':
        if number == 0:
            print("❌ Cannot divide by zero!")
            return memory
        return memory / number
    else:
        print("⚠️ Unknown operation")
        return memory

def load_memory(filename="memory.txt"):
    """Load last memory value from file, or start from 0 if not found."""
    try:
        with open(filename, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 0.0

def save_memory(memory, filename="memory.txt"):
    """Save current memory value to file."""
    with open(filename, "w") as f:
        f.write(str(memory))

if __name__ == "__main__":
    memory = load_memory()
    print(f"Current memory: {memory}")
    
    while True:
        user_input = input("Enter operation (+, -, *, /) and number, or 'exit' to quit: ").strip()
        
        if user_input.lower() == 'exit':
            save_memory(memory)
            print(f"💾 Memory saved! Final memory: {memory}")
            break
        
        try:
            operation, number = user_input.split()
            number = float(number)
            memory = calculate(memory, operation, number)
            print(f"Result: {memory}")
        except ValueError:
            print("⚠️ Invalid input. Example: + 5 or * 3")