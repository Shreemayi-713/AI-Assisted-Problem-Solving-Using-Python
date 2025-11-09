import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Simulated user database (in real use, store in a file or DB)
users = {}

# Register new user
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    users[username] = hash_password(password)
    print("User registered successfully!\n")

# Login function
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Main menu
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
