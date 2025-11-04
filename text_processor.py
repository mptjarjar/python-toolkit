# text_processor.py
# Day 1 - Your first Python tool

def clean_text(text):
    """Remove extra spaces and fix capitalization."""
    # Strip spaces at start/end, collapse internal multiple spaces
    cleaned = " ".join(text.split())
    # Capitalize first letter
    cleaned = cleaned.capitalize()
    return cleaned

# Example use
if __name__ == "__main__":
    user_text = input("Enter your text: ")
    result = clean_text(user_text)
    print("Cleaned text:", result)
