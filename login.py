# login.py
def login(username, password):
    # Example of hardcoded credentials (in a real-world case, use secure methods)
    stored_username = "user123"
    stored_password = "pass123"
    
    if username == stored_username and password == stored_password:
        return "Login successful"
    else:
        return "Invalid username or password"
