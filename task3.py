import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    print("Welcome to Password Generator")
    
    # Take input from the user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
