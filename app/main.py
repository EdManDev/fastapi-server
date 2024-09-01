# main.py
from fastapi import FastAPI
from app.api import articles #, categories, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(articles.router, prefix="/api/articles", tags=["articles"])
# app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
# app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI server"}



