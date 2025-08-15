from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db
from .. import models, schemas

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[schemas.ItemRead])
def list_items(db: Session = Depends(get_db)):
    return db.query(models.Item).order_by(models.Item.id).all()
