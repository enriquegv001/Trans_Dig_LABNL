from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

"""
Establishing connection between model and database table
Creating table of posts
"""

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))





from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/', response_model=List[schemas.CreatePost])
def test_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost])
def create_posts(post_create: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post_create.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]