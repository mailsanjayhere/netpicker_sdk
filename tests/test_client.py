import pytest
from netpicker_sdk.client import NetpickerClient

@pytest.fixture
def client():
    return NetpickerClient("admin@admin.com", "12345678", tenant="default", agent="DrkSpy")

def test_list_vaults(client):
    result = client.list_vaults()
    assert result["success"] is True
    assert isinstance(result["result"], list)

def test_list_devices(client):
    result = client.list_devices()
    assert "items" in result
    assert isinstance(result["items"], list)

def test_add_device(client):
    device = client.add_device(
        name="test-device-sdk",
        ip="192.0.2.1",
        platform="cisco_ios",
        vault="Cisco",
        tags=["pytest"]
    )
    assert "id" in device
    assert device["name"] == "test-device-sdk"

def test_trigger_backup(client):
    devices = client.list_devices()["items"]
    if not devices:
        pytest.skip("No devices available to trigger backup on.")
    device_id = devices[0]["id"]
    result = client.trigger_backup(device_id=device_id)
    assert result["success"] is True or result.get("status") == "ok"