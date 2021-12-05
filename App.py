from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_invoice'
mysql = MySQL(app)

app.secret_key = 'qwerty'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM  customer')
    data = cur.fetchall()
    return render_template('index.html', customers = data)

@app.route('/facturar/<id>')
def facturar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM facturas WHERE id_cli = {0}'.format(id))
    data = cur.fetchall()
    return render_template('facturar.html', invoices = data)


@app.route('/add', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        status = request.form['status']
        mobile = request.form['mobile']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO customer (id, name, status, mobile) VALUES (%s, %s, %s, %s)', (id,name, status, mobile))
        mysql.connection.commit()
        flash('Contacto Agregado de Forma Correcta')
        return redirect(url_for('Index'))


@app.route('/addfact', methods=['POST'])
def add_factura():
    if request.method == 'POST':
      date = request.form['date']
      id = request.form['idcli']
      price = request.form['price']
      balance = request.form['balance']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO facturas (fecha, id_cli, price, balance) VALUES (%s, %s, %s, %s)', (date, id, price, balance))
      mysql.connection.commit()
      flash('Factura Agregada de Forma Correcta')
      return redirect(url_for('Index'))
       
    
@app.route('/edit/<id>')
def editContact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM customer WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit.html', customers = data[0])


@app.route('/editfact/<number>')
def editFactura(number):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM facturas WHERE number = {0}'.format(number))
    data = cur.fetchall()
    return render_template('editfact.html', invoices = data)

@app.route('/update/<id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        mobile = request.form['mobile']       
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE customer
            SET name = %s,
                status = %s,
                mobile = %s
            WHERE id = %s
        """, (name, status, mobile, id))
        mysql.connection.commit()
        flash('Cliente Actualizado')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM customer WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Removido Satisfactoriamente')
    return redirect(url_for('Index'))

@app.route('/deletefact/<string:number>')
def delete_factura(number):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM facturas WHERE number = {0}'.format(number))
    mysql.connection.commit()
    flash('Factura Removida Satisfactoriamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)