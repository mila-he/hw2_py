from flask import Flask, render_template, request, redirect
from db.database import create_tables, drop_database, SessionLocal
from db.models import Television
from scraping.spider import parse
from utils.helpers import is_table_empty

app = Flask(__name__)

# Kuvab kõik tooted või otsingu tulemused
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter')
def filter_products():
    min_price = request.args.get('min_price', 0, type=float)
    db = SessionLocal()
    products = db.query(Television).filter(Television.price >= min_price).order_by(Television.price).all()
    db.close()
    return render_template('index.html', products=products, min_price=min_price)

# Kustuta andmebaas ja kraabi uuesti
@app.route('/drop')
def drop_and_recreate():
    drop_database()
    create_tables()
    parse('https://onoff.ee/et/35-televiisorid')
    return redirect('/')


if __name__ == '__main__':
    create_tables()
    if is_table_empty():
        print("Tabel on tühi, alustan kraapimist...")
        parse('https://onoff.ee/et/35-televiisorid')
    else:
        print("Tabelis on juba andmeid, kraapimist ei tehta.")
    app.run(debug=True)