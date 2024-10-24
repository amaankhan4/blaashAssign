from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models

router = APIRouter()

from ..database import SessionLocal
def get_db():
    print("get_db")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/posts/{tenant_id}", response_model=list[schemas.EngagementPostResponse])
def get_posts_for_tenant(tenant_id: int, db: Session = Depends(get_db)):
    posts = crud.get_engagement_post(db, tenant_id=tenant_id)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts

@router.post("/products", response_model=schemas.PostProductResponse)
def create_product(product: schemas.PostProductCreate, db: Session = Depends(get_db)):
    return crud.create_post_product(db=db, product=product)

@router.get("/")
def read_root():
    return {"Hello": "World"}
