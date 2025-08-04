import random
import string
def generate_password(length=12):
    if length < 4:
        print("Password length should be minimum 4 to include all character types.")
        return None
    # Define possible characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    # Ensure the password has minimum one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
                ]
    # Fill the remaining length with random choices from all sets combined
    if length > 4:
        all_characters = lowercase + uppercase + digits + symbols
        password += random.choices(all_characters, k=length - 4)
    # Shuffle the resulting list 
    random.shuffle(password) 
    # Convert list to string and return
    return ''.join(password)    
# Example usage
password_length = int(input("Enter the password length: "))
password = generate_password(password_length)
if password:
    print("Generated password:", password)