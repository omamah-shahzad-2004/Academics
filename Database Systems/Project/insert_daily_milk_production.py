from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def insert_milk_production():
    if request.method == 'POST':
        date = request.form.get('date')
        cowID = request.form.get('id')
        amMilkQuantity = request.form.get('amQty')
        noonMilkQuantity = request.form.get('noonQty')
        pmMilkQuantity = request.form.get('pmQty')

        cursor = conn.cursor()
        cursor.execute("INSERT INTO DailyMilkProduction (date, cowID, amMilkQuantity, noonMilkQuantity, pmMilkQuantity) VALUES (?, ?, ?, ?, ?)", (date, cowID, amMilkQuantity, noonMilkQuantity, pmMilkQuantity))
        cursor.commit()
        cursor.close()

    return render_template('daily_milk_production.html')
    