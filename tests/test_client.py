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
