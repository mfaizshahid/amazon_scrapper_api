from fastapi import FastAPI
import app.config.db
from app.routers import router
app = FastAPI()

app.include_router(router=router)


@app.get("/")
def hello_world():
    return {"Hello": "World"}
