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

if __name__ == "__main__":
    memory = 0.0
    print(f"Current memory: {memory}")
    
    while True:
        user_input = input("Enter operation (+, -, *, /) and number, or 'exit' to quit: ").strip()
        
        if user_input.lower() == 'exit':
            print(f"Goodbye! Final memory: {memory}")
            break
        
        try:
            operation, number = user_input.split()
            number = float(number)
            memory = calculate(memory, operation, number)
            print(f"Result: {memory}")
        except ValueError:
            print("⚠️ Invalid input. Example: + 5 or * 3")