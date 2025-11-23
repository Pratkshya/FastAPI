from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#define model item
class Items(BaseModel):
    name : str

#Acts like a small database
items = {'apple', 'kiwi', 'litchi'}

@app.delete("/items")
def delete_item(item: Items):
    name = item.name
    #delete the item
    items.remove(name)
    return {}
