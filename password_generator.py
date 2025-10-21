import random
import string

def generate_password(length, include_specials=True):
    # Character sets Definition
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation if include_specials else ""
    
    # Selected characters combination
    all_chars = lower + upper + digits + specials

    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Password Type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    if include_specials:
        password.append(random.choice(specials))

    
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle Patterns
    random.shuffle(password)
    
    #List to string Conversion
    return ''.join(password)


def main():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    choice = input("Include special characters? (y/n): ").strip().lower()
    include_specials = choice == 'y'

    password = generate_password(length, include_specials)
    if password:
        print("\n Generated Password:", password)


if __name__ == "__main__":
    main()
