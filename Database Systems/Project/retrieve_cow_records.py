from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def cow_records():
   if request.method == 'POST':
        id = request.form.get('search_bar')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CowRecords WHERE animalId = ?", (id, ))
        cow_data = cursor.fetchall()
        return render_template('cow_records.html', cow_data=cow_data)