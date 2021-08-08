from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is about page of {username}</h1>'

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