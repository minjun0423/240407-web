from typing import Union

from fastapi import FastAPI

app = FastAPI()

name = "minjun"

@app.get("/")
def read_root():
    return {"Hello": "World1"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

@app.post("/")
def create_root():
    return{"hello":"post"}

@app.put
def update_root():
    return{"hello":"put"}

@app.delete("/")
def delete_root():
    return {"hello":"delete"}