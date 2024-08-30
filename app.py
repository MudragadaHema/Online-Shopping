
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    product = request.form['product']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (name, email, product) VALUES (?, ?, ?)', (name, email, product))
    conn.commit()
    conn.close()

    return render_template('result.html', name=name, email=email, product=product)

if __name__ == '__main__':
    app.run()