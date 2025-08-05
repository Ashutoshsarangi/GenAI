# __name == __main__ example

# This is a simple example of how to use __name__ == '__main__' in Python.

def clean_text(text):
    return text.lower()

def tokenize_text(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello, World! This is a sample text."
    cleaned_text = clean_text(sample_text)
    tokenized_text = tokenize_text(cleaned_text)
    
    print("Cleaned Text:", cleaned_text)
    print("Tokenized Text:", tokenized_text)
# This if block will only execute if the script is run directly, 
#  not if it is imported as a module.