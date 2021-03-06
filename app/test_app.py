from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)


def test_shopee_item():
    payload = {"url": "https://shopee.co.id/Logitech-G102-Lightsync-Gaming-Mouse-i.39400356.3840449468"}
    response = client.post("/shopee/item", json=payload)
    assert response.status_code == 200
    assert "name" in response.json()

def test_shopee_shop():
    payload = {"url": "https://shopee.co.id/rovistar"}
    response = client.post("/shopee/shop", json=payload)
    assert response.status_code == 200
    assert "name" in response.json()
