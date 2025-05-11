# main.py

from fastapi import FastAPI, HTTPException
import sys
import os
# Ajoute le dossier courant au chemin
sys.path.append(os.path.dirname(__file__)) 
 
# On importe le modèle Item défini dans le fichier models.py
from models import Item  

# On crée une instance de l'application FastAPI
app = FastAPI()

# Une liste pour simuler une base de données (les données sont stockées en mémoire)
items_db = []


# On retourne tous les items enregistrés
@app.get("/items")
def get_all_items():
    return items_db



# On retourne un item selon son identifiant
@app.get("/items/{item_id}")
def get_item(item_id: int):
    
    # On cherche l'item correspondant dans la "base de données"
    for item in items_db:
        if item.id == item_id:
            return item
    # Si aucun item n'est trouvé, on renvoie une erreur 404
    
    
# POST /items - Ajoute un nouvel item
@app.post("/items")
def create_item(item: Item):
    # On vérifie si un item avec le même ID existe déjà
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Un item avec cet ID existe déjà")
    # Si l'ID est unique, on ajoute l'item à la liste
    items_db.append(item)
    return item



# PUT /items/{item_id} - Met à jour un item existant
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    # On parcourt la liste des items pour trouver celui à mettre à jour
    for index, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            # Remplace l'ancien item par le nouveau
            items_db[index] = updated_item
            return updated_item
    # Si l'item n'existe pas, on renvoie une erreur 404
    raise HTTPException(status_code=404, detail="Item non trouvé")


# DELETE /items/{item_id} - Supprime un item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # On essai de parcourir les items pour trouver celui à supprimer
    for item in items_db:
        if item.id == item_id:
            items_db.remove(item)
            return {"message": f"Item avec ID {item_id} supprimé"}
    # Si aucun item correspondant n'est trouvé, erreur 404
    raise HTTPException(status_code=404, detail="Item non trouvé")
