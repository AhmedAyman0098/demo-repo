#numeric validation
from fastapi import FastAPI , Path , Query

app = FastAPI()


@app.get("/")
async def root():
    return {"massage":"hello world"}


@app.get('/items/{item_id}')
async def get_item(item_id:int = Path(... , gt=1 ,lt=100,
                                       title="item_id" , description="the item id must be greater than or equal 1" )
                   ):
    return {"item_id":item_id}


@app.get("/items/")
async def get_item(
        min_price : float = Query(..., ge=1 , description=" price must be greater than 0"),
        max_price : float = Query(..., le=1000 , description="Maximum price must be less than or equal to 1000")
):
    return {"min_price":min_price,"max_price":max_price }