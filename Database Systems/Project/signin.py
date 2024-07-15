from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def signin_account():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM AdministratorLogin WHERE username=? AND password=?", (username, password))
        administrator = cursor.fetchone()

        if administrator:
            session['username'] = administrator[0]
            session['password'] = administrator[1]
            return redirect('daily_milk_production.html')

    return render_template('Home.html')