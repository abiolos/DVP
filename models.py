# Fichier models.py

from pydantic import BaseModel

# Cette classe définit le modèle de données "Item"

class Item(BaseModel):
    # L'identifiant unique de l'item
    id: int  
    # Le nom de l'item         
    name: str  
    # Le prix de l'item       
    price: float    
    # Si l'item est en stock ou non  
    in_stock: bool    
