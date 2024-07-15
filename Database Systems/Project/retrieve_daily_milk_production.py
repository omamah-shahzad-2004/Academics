from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def milk_production():
   if request.method == 'POST':
        id = request.form.get('searchbar')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DailyMilkProduction WHERE cowID = ?", (id, ))
        milk_data = cursor.fetchall()
        return render_template('daily_milk_production.html', milk_data=milk_data)
