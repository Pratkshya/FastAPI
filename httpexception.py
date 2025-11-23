from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str

items = {'apple', 'mango', 'litchi'}

@app.delete("/items")
def delete_item(item : Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        #raise HTTPException error when item not found
        raise HTTPException(status_code=404, detail="items not found")
    return {}