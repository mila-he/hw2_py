from sqlalchemy import Column, Integer, String, Float
from db.database import Base

class Television(Base):
    __tablename__ = 'televisions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=False)