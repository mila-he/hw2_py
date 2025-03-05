from sqlalchemy import Column, Integer, String
from db.database import Base


# ORM tabeli mudel
class Television(Base):
    __tablename__ = 'televisions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    image = Column(String, nullable=False)