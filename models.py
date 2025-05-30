from sqlalchemy import Column, Integer, String
from database import Base

class Contact(Base):
    __tablename__ = "create_contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    country = Column(String, nullable=True)
    message = Column(String, nullable=True)
