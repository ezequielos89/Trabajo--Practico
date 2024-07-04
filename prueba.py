from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#MySQL Connection

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'trabajo_practico'

mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM info_de_contactos')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id_contacto = request.form['id_contacto']
        nombre_apellido = request.form['nombre_apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO info_de_contactos (id_contacto, nombre_apellido, email, telefono) VALUES (%s, %s, %s, %s)',
                    (id_contacto, nombre_apellido, email, telefono))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        
        return redirect(url_for('index'))


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM info_de_contactos WHERE id_contacto = %s', (id,))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        id_contacto = request.form['id_contacto']
        nombre_apellido = request.form['nombre_apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE info_de_contactos
            SET id_contacto = %s,
                nombre_apellido = %s,
                email = %s,
                telefono = %s
            WHERE id_contacto = %s
            """, (id_contacto, nombre_apellido, email, telefono, id))
        
        mysql.connection.commit()
        flash('Contacto editado satisfactoriamente')
        
        return redirect(url_for('index'))

   
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM info_de_contactos WHERE id_contacto = %s',(id,))
    mysql.connection.commit()
    flash('Contacto eliminado satisfactoriamente')
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)
