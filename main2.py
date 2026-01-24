from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


from enum import Enum

@app.get("/")
async def root():
    return {"massage":"hello world"}

items = [
    {"id":1 , "name":"book" , "price":"15" , "stock":True},
    {"id":2 , "name":"game" , "price":"50", "stock":True},
    {"id":3 , "name":"cd" , "price":"30", "stock":True},
    {"id":4 , "name":"magazine" , "price":"10" , "stock":False},
    {"id":5 , "name": "book" , "price":"10" , "stock": True},
    {"id":6 , "name": "game" , "price":"10" , "stock":True}
]

@app.get("/items")
async def list_items(
        start : int = 0 ,
        end :int =10 ,
        id : int = None,
        name: str = None
):
        
    if id:
        item = next((item for item in items if item["id"]==id),None)
        if item :
            return item
        else:
            return {"massage":"item not found"}
    if name:
        filtered=[]
        for item in items :
            if item["name"] == name :
                filtered.append(item)
        return filtered

    return items[start:start+end]


@app.get("/items/prices")
async def sort_price(range : int = None):
    sorted_price = sorted(items , key= lambda x:x["price"], reverse=True)

    if range:
        price_range = [item for item in sorted_price if item["price"] <= str(range) ]
        
        return price_range
    else:
        return sorted_price

@app.get("/items/stock")
async def get_stock(in_stock:bool = True):
    if not in_stock:
        item = [item for item in items if item ["stock"] == False]

        return item
    
    else:
        item = [item for item in items if item ["stock"] == True]
        return item


class item(BaseModel):
    items:str
    description : str|None = None
    prise : float
    tax : float | None = None

@app.post("/items")
async def create_item(item:item):
    item_dict = item.dict()
    if item.tax:

        price_with_tax = item.prise + (item.prise*item.tax)
        item_dict.update({"total_price":price_with_tax})


    return item_dict   

@app.put("/items/{item_id}")
async def update_item(item_id:int , item:item):
    return {"item_id":item_id, **item.dict()}