# app/routes/collection_routes.py
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


@router.post("/collections", response_model=schemas.CollectionResponse)
async def create_collection(collection: schemas.CollectionCreate, db: Session = Depends(get_db)):
    return crud.create_collection(db, collection)
