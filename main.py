from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Contact
from schemas import ContactCreate
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Create the DB tables if they don't exist
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contacts", status_code=201)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://smartshopie.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = Contact(
        first_name=contact.first_name,
        last_name=contact.first_name,
        email=contact.email,
        phone=contact.phone,
        country=contact.country,
        message=contact.message
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Contact created successfully", "id": new_contact.id}
