from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.String(length=20), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'Item {self.name}'



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id':1, 'name': 'Phone', 'barcode': '1124', 'price': 500},
        {'id':2, 'name': 'Laptop', 'barcode': '6938', 'price': 800},
        {'id':3, 'name': 'Keyboard', 'barcode': '4342', 'price': 140}
    ]
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)