from fastapi import FastAPI, Depends
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI project running successfully"}


# createUser
@app.post("/user_create")
def CreateUser(user: schemas.UserformSchema, db :Session=Depends(get_db)):
    db_user = models.UserForm(name=user.name, email=user.email, message=user.message)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
