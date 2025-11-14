from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'equipment.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    category = request.args.get('category','')

    if category:
        equipments = conn.execute('SELECT * FROM equipments WHERE category = ?', (category,)).fetchall()
    else:
        equipments = conn.execute('SELECT * FROM equipments').fetchall()

    categories = conn.execute('SELECT DISTINCT category FROM equipments').fetchall()
    conn.close()

    return render_template('index.html', equipments=equipments, categories=categories, selected_category=category)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        rental_fee = request.form['rental_fee']
        quantity = request.form['quantity']
        availability = request.form['availability']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO equipments (name, category, rental_fee, quantity, availability) VALUES (?, ?, ?, ?, ?)',
                     (name, category, rental_fee, quantity, availability))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        rental_fee = request.form['rental_fee']
        quantity = request.form['quantity']
        availability = request.form['availability']
        
        conn.execute('UPDATE equipments SET name = ?, category = ?, rental_fee = ?, quantity = ?, availability = ? WHERE id = ?',
                     (name, category, rental_fee, quantity, availability, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    equipment = conn.execute('SELECT * FROM equipments WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    return render_template('edit.html', equipment=equipment)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM equipments WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)