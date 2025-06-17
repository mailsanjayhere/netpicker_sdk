from .auth import Auth
import requests

class NetpickerClient:
    def __init__(self, username, password, tenant="default", agent="DrkSpy"):
        self.auth = Auth(username, password)
        self.tenant = tenant
        self.agent = agent
        self.base_url = f"https://sandbox.netpicker.io/api/v1/agents/{tenant}/{agent}"

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.auth.get_token()}",
            "Content-Type": "application/json"
        }

    def create_vault(self, name, username, password):
        url = f"{self.base_url}/vaults/"
        payload = {
            "name": name,
            "username": username,
            "password": password
        }
        res = requests.post(url, json=payload, headers=self._headers())
        res.raise_for_status()
        return res.json()

    def list_vaults(self):
        url = f"https://sandbox.netpicker.io/api/v1/agents/{self.tenant}/{self.agent}/vaults"
        res = requests.get(url, headers=self._headers())
        res.raise_for_status()
        return res.json()

    def list_devices(self):
        url = f"https://sandbox.netpicker.io/api/v1/devices/{self.tenant}"
        res = requests.get(url, headers=self._headers())
        res.raise_for_status()
        return res.json()

    def add_device(self, name, ip, platform, vault, tags=None):
        url = f"https://sandbox.netpicker.io/api/v1/devices/{self.tenant}"
        payload = {
            "name": name,
            "ip": ip,
            "platform": platform,
            "vault": vault,
            "tags": tags or []
        }
        res = requests.post(url, json=payload, headers=self._headers())
        res.raise_for_status()
        return res.json()

    def trigger_backup(self, device_id):
        url = f"https://sandbox.netpicker.io/api/v1/backup/{self.tenant}"
        payload = {
            "device_id": device_id
        }
        res = requests.post(url, json=payload, headers=self._headers())
        res.raise_for_status()
        return res.json()