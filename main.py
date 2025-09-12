from typing import Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello World!"}

# @app.get('/greet/{username}')
# async def greet(username:str):
#    return {"message":f"Hello {username}"}

user_list = ["Alice", "Bob", "Charlie"]
@app.get('/search/')
async def search_for_user(username: str):
    if username in user_list:
        return {"message": f"User {username} found!"}
    return {"message": f"User {username} not found."}

@app.get('/greet/')
async def greet(username:Optional[str]="User"):
   return {"message":f"Hello {username}"}




# the User model
class UserSchema(BaseModel):
   username:str
   email:str


@app.post("/create_user")
async def create_user(user_data:UserSchema):
   new_user = {
      "username" : user_data.username,
      "email": user_data.email
   }

   users = []

   users.append(new_user)

   return {"message":"User Created successfully","user":new_user}


# inside main.py
@app.get('/get_headers')
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Accept-Language"] = accept_language
    request_headers["Connection"] = connection
    request_headers["Host"] = host

    return request_headers