from bottle import Bottle, template, request, redirect, static_file
import sqlite3

app = Bottle()

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page - List all customers
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    customers = cur.fetchall()
    conn.close()
    return template('index', customers=customers)

# Route to display form to add a new customer
@app.route('/add', method='GET')
def add_customer_form():
    return template('add_customer')

# Route to process the form data and add a new customer
@app.route('/add', method='POST')
def add_customer():
    name = request.forms.get('name')
    email = request.forms.get('email')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return redirect('/')

# Route to display form to edit an existing customer
@app.route('/edit/<id:int>', method='GET')
def edit_customer_form(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE id = ?", (id,))
    customer = cur.fetchone()
    conn.close()

    return template('edit_customer', customer=customer)

# Route to process the form data and update the customer
@app.route('/edit/<id:int>', method='POST')
def edit_customer(id):
    name = request.forms.get('name')
    email = request.forms.get('email')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE customers SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    conn.close()

    return redirect('/')

# Route to delete a customer
@app.route('/delete/<id:int>')
def delete_customer(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')

# Static file route example for CSS, JS, etc.
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    app.run(host='localhost', port=8083, debug=True, reloader=True)

