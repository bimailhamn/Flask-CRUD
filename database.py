from flask_mysqldb import MySQL
from flask import request,redirect,url_for,session,flash

class CRUD(MySQL):
    def read(self):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT  * FROM karyawan ''')
        z = cursor.fetchall()
        cursor.close()
        return z

    def signup(self):
        cursor = self.connection.cursor()
        remail = request.form['remail']
        rpassword = request.form['rpassword']
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO login(email,password) VALUES(%s,%s)''',(remail,rpassword))
        self.connection.commit()
        cursor.close()
    
    def login(self):
        cursor = self.connection.cursor()
        email = request.form['accountemail']
        password = request.form['accountpassword']
        cursor.execute(''' SELECT  * FROM login where email=%s and password=%s ''',(email,password))
        pool = {"login": cursor.fetchone(),"email": email,"password":password}
        return pool

    def create(self):
        nama = request.form['nama']
        divisi = request.form['divisi']
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO karyawan(NAMA,DIVISI) VALUES(%s,%s)''',(nama,divisi))
        self.connection.commit()
        cursor.close()
        flash('Data added successfully','success')
    
    def delete1(self,id):
        cursor = self.connection.cursor()
        cursor.execute('''
        DELETE 
        FROM karyawan
        WHERE ID=%s''', (id, ))
        self.connection.commit()
        cursor.close()
        flash('Data deleted successfully','success')
    
     
    def get(self,id):
        cursor = self.connection.cursor()
        cursor.execute('''
        SELECT * 
        FROM karyawan 
        WHERE ID =%s''', (id, ))
        karyawan = cursor.fetchone()
        cursor.close()
        return karyawan

    def post(self,id):
        nama = request.form['nama']
        divisi = request.form['divisi']
        cursor = self.connection.cursor()
        cursor.execute(''' 
        UPDATE karyawan 
        SET 
        nama = %s,
        divisi = %s
        WHERE
        id = %s
        ''',(nama,divisi,id))
        self.connection.commit()
        cursor.close()
        flash('Data updated successfully','success')
    
        




    
