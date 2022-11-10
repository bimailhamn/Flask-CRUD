from flask import Flask,render_template,url_for, redirect, request, session, flash
from database import CRUD
import json

#inisiasi object app
app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'nexin'
mysql = CRUD(app)

#endpoint register
@app.route("/register", methods=['GET','POST'])
def register():
    if 'email' in session:
        return redirect(url_for('karyawan'))
    else:
        if request.method == 'GET':
            return render_template('register.html')
        else:
            mysql.signup()
            return redirect(url_for('home'))

   
@app.route("/", methods=['GET','POST'])
def home():
    if 'email' in session:
        return redirect(url_for('karyawan'))
    else:
        if request.method == 'GET':
            return render_template("home.html")
        else:
            mysql.login()
            data = mysql.login()
            if data["login"] is not None:
                session['email'] = data["email"]
                session['password'] = data["password"]
                return redirect(url_for('karyawan'))

            else:
                notif = "email dan password salah"
                return render_template("home.html",notif = notif)
    
@app.route("/karyawan")
def karyawan():
    if 'email' in session:
        karyawan = mysql.read()
        return render_template("index.html",karyawan = karyawan )
    else:
        return redirect(url_for('home'))




@app.route('/karyawan/tambah', methods=['GET', 'POST'])
def tambah():
    if 'email' in session:
        if request.method == 'GET':
            return render_template('tambah.html')
        else:
            mysql.create()
            return redirect(url_for('karyawan'))

        return render_template('index.html')
    else:
        return redirect(url_for('home'))

@app.route('/karyawan/edit/<int:id>', methods=['GET', 'POST'])
def editkaryawan(id):
    if request.method == 'GET':
        mysql.get(id)
        karyawan = mysql.get(id)
        return render_template('edit.html', karyawan = karyawan)
    else:
        mysql.post(id)
        return redirect(url_for('karyawan'))

    return render_template('index.html')

@app.route('/karyawan/delete/<int:id>', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        mysql.delete1(id)
        return redirect(url_for('karyawan'))

    return render_template('karyawan.html')

@app.route("/logout")
def logout():
    session.pop('email')
    session.pop('password')
    return redirect(url_for('home'))

@app.route("/testjson")
def testjson():
    datajson = mysql.read()
    y = [data for data in datajson]
    return y


@app.route("/api/login", methods=['POST'])
def login_api():
    posted_data = request.json
    email = posted_data['email']
    password = posted_data['password']
    data = CRUD.login(email, password)

if __name__ == "__main__":
    app.run(debug=True)

