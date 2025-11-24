from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# define model Item
class Items(BaseModel):
    name : str
    quantity : Optional[int] = 0 #default value and quatity field is optional

items = {"boxes": Items(name= 'boxes', quantity=20)}

@app.get("/items")
def read(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]