import string
import random

def generate_password(length, char_set):
    password = "".join(random.choice(char_set) for i in range(length))
    return password

def get_character_set(use_letters, use_numbers, use_symbols):
    char_set = ""
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    return char_set

def main():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Invalid length. Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    use_letters = input("Use letters? (y/n): ").lower() == "y"
    use_numbers = input("Use numbers? (y/n): ").lower() == "y"
    use_symbols = input("Use symbols? (y/n): ").lower() == "y"

    if not use_letters and not use_numbers and not use_symbols:
        print("Error: At least one character type must be selected.")
        return

    char_set = get_character_set(use_letters, use_numbers, use_symbols)
    password = generate_password(length, char_set)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()