# text_processor.py
# Day 1 - My first Python tool

def clean_text(text):
    """Remove extra spaces and fix capitalization."""
    cleaned = " ".join(text.split())  # collapse extra spaces
    cleaned = cleaned.capitalize()    # capitalize first letter
    return cleaned

if __name__ == "__main__":
    # Ask the user for input
    user_text = input("Enter your text: ")
    
    # Clean the text
    result = clean_text(user_text)
    print("Cleaned text:", result)
    
    # Ask if they want to save it
    answer = input('Would you like to save the cleaned text? Type "yes" to proceed: ')
    
    if answer.lower() == "yes":
        # Write to file
        with open("cleaned_output.txt", "w") as f:
            f.write(result)
        print("✅ Cleaned text saved as cleaned_output.txt")
    else:
        print("No file saved.")
