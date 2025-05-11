# test_main.py

from fastapi.testclient import TestClient
from main import app

# On crée un client de test à partir de l'app FastAPI
client = TestClient(app)

def test_read_empty_items():
    # On teste que la base est vide au départ
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    # On crée un nouvel item
    item_data = {
        "id": 1,
        "name": "Ibidun",
        "price": 50,
        "in_stock": True
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_get_item_by_id():
    # On récupère l'item qu'on a ajouté juste avant
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Ibidun"

def test_update_item():
    # On met à jour l'item existant
    updated_data = {
        "id": 1,
        "name": "AJAGBE Ibidun",
        "price": 70.00,
        "in_stock": False
    }
    response = client.put("/items/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Clavier mécanique"

def test_delete_item():
    # On supprime l'item
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert "supprimé" in response.json()["message"].lower()

def test_item_not_found():
    # On essaie de récupérer un item inexistant
    response = client.get("/items/300")
    assert response.status_code == 404
