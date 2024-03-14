import os
import hashlib
import base64

class KeyManagement:
    def __init__(self):
        self.users_keys = {}  # Placeholder for storing user keys

    def generate_key(self, username):
        # Generate key for the user (This can be implemented using cryptographic libraries)
        key = "randomly_generated_key"
        self.users_keys[username] = key
        return key
    
    def save_key(self, public_key, private_key, filename="keys.txt"):
        """
        Save the generated keys to a file.
        """
        with open(filename, "wb") as file:
            file.write(base64.b64encode(public_key))
            file.write(b"\n")
            file.write(base64.b64encode(private_key))

    def load_key(self, filename="keys.txt"):
        """
        Load keys from a file.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")

        with open(filename, "rb") as file:
            public_key_b64 = file.readline().strip()
            private_key_b64 = file.readline().strip()

        public_key = base64.b64decode(public_key_b64)
        private_key = base64.b64decode(private_key_b64)
        return public_key, private_key
