from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# define model Item
class Item(BaseModel):
    name: str
    quantity: Optional[int] = 0

items = {}

#Create
@app.post("/items")
def create(item : Item):
    name = item.name
    if name in items:
        raise HTTPException(status_code=409, detail="Item exists")
    items[name] = item
    return {"message": f"Added {name} to items."}

#Read
@app.get("/items")
def read(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]  

#Update
@app.put("/items")
def update(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[name] = item
    return {"message": f"Updated {name}."}

#Delete
@app.delete("/items")
def delete(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[name]
    return {"message": f"Deleted {name}."}