# app/routes/post_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas

router = APIRouter()

from ..database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/posts/top-viewed/{tenant_id}", response_model=list[schemas.TopViewedPostResponse])
def get_top_viewed_posts(tenant_id: int, db: Session = Depends(get_db)):
    top_posts = crud.get_top_viewed_posts(db, tenant_id=tenant_id)
    return top_posts

@router.get("/products/top-viewed/{tenant_id}", response_model=list[schemas.TopViewedProductResponse])
def get_top_viewed_products(tenant_id: int, db: Session = Depends(get_db)):
    return crud.get_top_viewed_products(db, tenant_id=tenant_id)
