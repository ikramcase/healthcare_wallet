# main.py
from authentication import AuthenticationManager
from key_management import KeyManagement

if __name__ == "__main__":
    auth_manager = AuthenticationManager()
    keys_manager = KeyManagement()

    # Register and authenticate users
    auth_manager.register_user("user1", "password1")
    auth_manager.register_user("user2", "password2")

    auth_manager.authenticate_user("user1", "password1")
    auth_manager.authenticate_user("user2", "password123")  # Incorrect password

    # Generate keys for users
    user1_key = keys_manager.generate_key("user1")
    user2_key = keys_manager.generate_key("user2")

    print("Keys generated for user1:", user1_key)
    print("Keys generated for user2:", user2_key)
