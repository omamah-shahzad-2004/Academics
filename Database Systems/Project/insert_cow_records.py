from flask import request, session, render_template, redirect
from dbconn import db_conn

conn = db_conn()

def insert_cow_records():
    if request.method == 'POST':
        animal_id = request.form.get('ani_id')
        ear_id = request.form.get('ear_id')
        animal_type = request.form.get('ani_type')
        color = request.form.get('color')
        breed = request.form.get('breed')
        birth_date = request.form.get('bdate')
        weight_at_birth = request.form.get('weight_birth')

        cursor = conn.cursor()
        cursor.execute("INSERT INTO CowRecords (animalID, earID, animalType, color, breed, birthDate, weightAtBirth) VALUES (?, ?, ?, ?, ?, ?, ?)", (animal_id, ear_id, animal_type, color, breed, birth_date, weight_at_birth))
        cursor.commit()
        cursor.close()

    return render_template('cow_records.html')