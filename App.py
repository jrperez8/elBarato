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
    return render_template('index.html')

@app.route('/clientes')
def Clientes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM  customer')
    data = cur.fetchall()
    return render_template('clientes.html', customers = data)

@app.route('/facturar')
def facturar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM facturas')
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
        return redirect(url_for('Clientes'))


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
      return redirect(url_for('facturar'))
       
    
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def editContact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM customer WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit.html', customers = data[0])


@app.route('/editfact/<number>', methods = ['POST', 'GET'])
def editFactura(number):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM facturas WHERE number = %s', [number])
    data2 = cur.fetchall()
    cur.close()
    return render_template('editfact.html', invoices = data2[0])

@app.route('/update/<id>', methods = ['POST', 'GET'])
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
        return redirect(url_for('Clientes'))

@app.route('/updatefact/<number>', methods = ['POST' , 'GET'])
def updatefact(number):
    if request.method == 'POST':
        #number = request.form['number']
        date = request.form['date']
        idcli = request.form['idcli'] 
        price = request.form['price']  
        balance = request.form['balance']        
        cur = mysql.connection.cursor()
        cur.execute("""
             UPDATE facturas
             SET fecha = %s,
                 id_cli = %s,
                 price = %s,
                 balance = %s
           WHERE number = %s
         """, (date, idcli, price, balance, number))
        mysql.connection.commit()
        flash('Factura Actualizada')
        return redirect(url_for('facturar'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM customer WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Removido Satisfactoriamente')
    return redirect(url_for('Clientes'))

@app.route('/deletefact/<string:number>')
def delete_factura(number):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM facturas WHERE number = {0}'.format(number))
    mysql.connection.commit()
    flash('Factura Removida Satisfactoriamente')
    return redirect(url_for('facturar'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)