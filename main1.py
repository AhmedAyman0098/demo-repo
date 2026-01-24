from fastapi import FastAPI

app = FastAPI()


from enum import Enum

@app.get("/")
async def root():
    return {"massage":"hello world"}

@app.post("/")
async def post():
    return {"massage":"this is a post request"}


@app.get("/users")
async def list_users():
    return {"massage":"this is user list"}



@app.get("/users/1" , include_in_schema=False)
async def admin_user():
    return {"massage":"this is the admin portal"}



@app.get("/users/{user_id}")
async def get_user(user_id : int):
    return {"user id":user_id}




class usersList(str ,Enum):
    admin = 1
    manger = 2
    user = 3

@app.get("/{user_type}/{user_id}")
async def get_user_type(user_type : usersList , user_id):
    return{"user": {user_type.name , user_id}}