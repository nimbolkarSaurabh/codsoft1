import random
import string

def generate_password(length, complexity):
    if complexity == 'Easy':
        characters = string.ascii_lowercase
    elif complexity == 'Medium':
        characters = string.ascii_letters
    elif complexity == 'Strong':
        characters = string.ascii_letters + string.digits
    elif complexity == 'Ultra-Strong':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Using default complexity (Strong).")
        characters = string.ascii_letters + string.digits

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a valid password length greater than 0.")
                continue  # Continue the loop to get valid input

            print("Choose the complexity level:")
            print("1. Easy (lowercase letters only)")
            print("2. Medium (uppercase + lowercase letters)")
            print("3. Strong (uppercase + lowercase letters + digits)")
            print("4. Ultra-Strong (uppercase + lowercase letters + digits + special characters)")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '5':
                print("Exiting the password generator. Goodbye!")
                break  # Exit the loop

            if choice in ('1', '2', '3', '4'):
                if choice == '1':
                    complexity = 'Easy'
                elif choice == '2':
                    complexity = 'Medium'
                elif choice == '3':
                    complexity = 'Strong'
                elif choice == '4':
                    complexity = 'Ultra-Strong'
                password = generate_password(length, complexity)
                print("Generated Password:", password)
            else:
                print("Invalid choice. Using default complexity (Strong).")
                complexity = 'Strong'
                password = generate_password(length, complexity)
                print("Generated Password:", password)
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")

if _name_ == "_main_":
    main()