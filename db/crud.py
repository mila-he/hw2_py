from sqlalchemy.orm import Session
from db.database import SessionLocal, create_tables
from db.models import Television

def save_to_db(data):
    db: Session = SessionLocal()
    try:
        # Kontrollime, kas sama nimega toode on juba olemas
        existing = db.query(Television).filter_by(name=data['name']).first()
        if existing:
            print(f"Toode '{data['name']}' on juba andmebaasis.")
        else:
            new_tv = Television(name=data['name'], price=data['price'], image=data['image'])
            db.add(new_tv)
            db.commit()
            print(f"Salvestatud: {data['name']}")
    except Exception as e:
        db.rollback()
        print("Viga salvestamisel:", e)
    finally:
        db.close()

# Otsi kõik tooted
def get_all_tvs():
    db: Session = SessionLocal()
    try:
        results = db.query(Television).all()
        return results
    finally:
        db.close()