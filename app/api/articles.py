from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.article import Article, ArticleCreate
from app.services import article as article_service

router = APIRouter()

@router.post("/")
async def post_article():
    return {"message": "post article"}

@router.get("/")
def read_articles():
    return {"message": "get article"}

@router.get("/{article_id}", response_model=dict)
def read_article(article_id: int):
    return {"message": f"get id: {article_id}"}

@router.put("/{article_id}", response_model=dict)
def update_article(article_id: int):
    return {"message": f"put id: {article_id}"}

@router.delete("/{article_id}", response_model=dict)
def remove_article(article_id: int):
    return {"message": f"delete id: {article_id}"}