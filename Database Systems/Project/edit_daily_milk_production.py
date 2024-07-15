from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def update_milk_production(date, id):
    if request.method == 'POST':
        date = request.form.get('date')
        cowID = request.form.get('id')
        amMilkQuantity = request.form.get('amQty')
        noonMilkQuantity = request.form.get('noonQty')
        pmMilkQuantity = request.form.get('pmQty')

        cursor = conn.cursor()
        cursor.execute("UPDATE DailyMilkProduction SET amMilkQuantity=?, noonMilkQuantity=?,pmMilkQuantity=? WHERE date=? AND cowID=?", (amMilkQuantity, noonMilkQuantity, pmMilkQuantity, date, cowID))
        conn.commit()
    return render_template('daily_milk_production.html')