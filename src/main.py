from fastapi import FastAPI
import app.config.db
app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}
