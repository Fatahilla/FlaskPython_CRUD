from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', computers=rv)

@app.route('/save',methods=["POST"])
def save():
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s)",(nama,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET data=%s WHERE id=%s", (nama,id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id_data>', methods=["GET"])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("Delete FROM computer WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)