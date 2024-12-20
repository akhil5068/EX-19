def login(username, password):
    # Simulate login verification
    if username == "admin" and password == "password123":
        return "Login successful!"
    return "Invalid credentials."

# Example usage
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))
