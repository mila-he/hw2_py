from db.database import SessionLocal
from db.models import Television

# Kontrollib, kas tabel on tühi
def is_table_empty():
    db = SessionLocal()
    try:
        return db.query(Television).first() is None
    finally:
        db.close()

