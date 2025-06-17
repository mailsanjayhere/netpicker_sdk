# Netpicker SDK for Python

A lightweight Python SDK for interacting with the [Netpicker](https://netpicker.io) API.

This SDK allows developers and network engineers to automate tasks such as authentication, vault management, device onboarding, and triggering configuration backups — all from Python.

---

## 📦 Features

- ✅ Authenticate via JWT using username/password
- 🔐 List and use vaults (pre-configured in the agent)
- 🖥️ List and add devices
- 💾 Trigger configuration backups
- ⚙️ Easily extendable for other Netpicker endpoints

---

## 🛠 Installation

We recommend using a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ./netpicker_sdk
```

---

## 🧪 Usage Example

```python
from netpicker_sdk.client import NetpickerClient

client = NetpickerClient("admin@admin.com", "12345678", tenant="default", agent="DrkSpy")

# List vaults
vaults = client.list_vaults()
print("Vaults:", vaults)

# List devices
devices = client.list_devices()
print("Devices:", devices)

# Add a device
device = client.add_device(
    name="test-device",
    ip="192.168.1.1",
    platform="cisco_ios",
    vault="Cisco",
    tags=["lab"]
)
print("Device added:", device)

# Trigger a backup
backup = client.trigger_backup(device_id=device["id"])
print("Backup started:", backup)
```

---

## 🔧 Project Structure

```
netpicker_sdk/
├── netpicker_sdk/
│   ├── __init__.py
│   ├── auth.py
│   ├── client.py
├── setup.py
├── README.md
```

---

## 📄 License

MIT License (add `LICENSE` file to define terms).
