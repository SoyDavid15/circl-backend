from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login():
    return "hola"