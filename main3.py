#validate_item@
from fastapi import FastAPI
from fastapi import Query

app = FastAPI()


@app.get("/")
async def root():
    return {"massage":"hello world"}

@app.get("/items")
async def read_items(name : str = "unknown"):
    return {"name":name}

@app.get("/validate")
async def validate_item(name:str = Query ( ... , min_length= 3 , max_length=50 ,regex=r"^[a-zA-Z\s]+$"),
                        email:str = Query(... , min_length=3, max_length=50 , regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")):
    return {"name":name , "email": email}
