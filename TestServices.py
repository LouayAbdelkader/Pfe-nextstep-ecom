import requests
import pytest

USER_SERVICE_URL = "http://10.9.21.20:30001"
PRODUCT_SERVICE_URL = "http://10.9.21.20:30002"

def test_signup():
    response = requests.post(f"{USER_SERVICE_URL}/signup", json={"username": "testuser", "password": "testpass"})
    assert response.status_code in [201, 409]  # 201 si succès, 409 si utilisateur existe déjà

def test_login():
    response = requests.post(f"{USER_SERVICE_URL}/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "message" in response.json()

def test_login_fail():
    response = requests.post(f"{USER_SERVICE_URL}/login", json={"username": "wronguser", "password": "wrongpass"})
    assert response.status_code == 401

def test_get_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    assert response.status_code == 200
    assert "products" in response.json()
    assert isinstance(response.json()["products"], list)

if __name__ == "__main__":
    pytest.main()
