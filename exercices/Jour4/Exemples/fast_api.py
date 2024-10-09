from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialiser la base de données
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Modèle de la base de données
class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


# Créer la base de données
Base.metadata.create_all(bind=engine)


# Modèle Pydantic pour validation des données
class Item(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


app = FastAPI()


# Récupérer la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route pour récupérer tous les items (Read)
@app.get("/items", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 10, db=SessionLocal()):
    items = db.query(ItemDB).offset(skip).limit(limit).all()
    return items


# Route pour créer un nouvel item (Create)
@app.post("/items", response_model=Item)
def create_item(item: Item, db=SessionLocal()):
    db_item = ItemDB(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Route pour récupérer un item par ID (Read)
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, db=SessionLocal()):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Route pour mettre à jour un item (Update)
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db=SessionLocal()):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item


# Route pour supprimer un item (Delete)
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db=SessionLocal()):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
