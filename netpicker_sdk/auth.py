import requests
import time

class Auth:
    def __init__(self, username, password):
        self.url = "https://sandbox.netpicker.io/api/v1/auth/jwt/login"
        self.username = username
        self.password = password
        self.token = None
        self.expiry = 0

    def login(self):
        response = requests.post(
            self.url,
            headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
                "scope": "",
                "client_id": "string",
                "client_secret": "string"
            }
        )
        response.raise_for_status()
        data = response.json()
        print("[DEBUG] Login response:", data)
        self.token = data["access_token"]
        self.expiry = time.time() + 3600  # assume 1 hour expiry

    def get_token(self):
        if not self.token or time.time() > self.expiry - 300:
            self.login()
        return self.token
