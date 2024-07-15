from flask import request, session, render_template, redirect, url_for
from dbconn import db_conn

conn = db_conn()

def delete_milk_production(date, id):
   cursor = conn.cursor()
   cursor.execute("DELETE FROM DailyMilkProduction WHERE cowID = ? AND date = ?", (id, date))
   cursor.execute("SELECT * FROM DailyMilkProduction WHERE cowID = ?", (id))
   milk_data = cursor.fetchall()
   conn.commit()
   return render_template('daily_milk_production.html', milk_data=milk_data)
