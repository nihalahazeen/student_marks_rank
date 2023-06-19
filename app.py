from fastapi import FastAPI

from config.config import initiate_database
from src.routes.student import router as StudentRouter
from src.routes.rank import router as RankRouter

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the app."}


app.include_router(StudentRouter, tags=["Students"], prefix="/student")
app.include_router(RankRouter, tags=["Rank"], prefix="/rank")
