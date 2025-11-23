from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name : str

@app.post("/")
#end point function
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}