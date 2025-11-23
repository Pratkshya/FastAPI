from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str

# behaves like a in-memory database
items = {"apple": "A red fruit"}

@app.put("/items")
def update_item(item: Item):
    name = item.name
    items[name] = item.description #Updates with the new data or creates if doesn't exist
    return item