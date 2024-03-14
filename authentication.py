class AuthenticationManager:
    def __init__(self):
        self.users = {}  # Placeholder for storing users and their passwords

    def register_user(self, username, password):
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = password
            print("User registered successfully.")

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False