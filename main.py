from fastapi import FastAPI , Path , Query , Body
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def root():
    return {"massage":"hello world"}


class item(BaseModel):
    name : str  
    description : str       
    price : float

class User(BaseModel):
    username : str
    full_name : str

#class age(BaseModel):
#    age : int



@app.put('/items/{item_id}')
async def update_item(
        *,
        item_id : int = Path(... , title="the item id ", ge= 0 , le=100),   
        q : str | None = None,
        item : item | None = None,
        user : User | None =None,  
        age : int = Body(...)
):          
    result = {"item_id": item_id}

    if q: 
        result.update ({"q":q})
    if item:
        result.update ({"item" : item}) 
    if user:
        result.update({"user": user})
    if age: 
        result.update({"age": age})

    
    return result       