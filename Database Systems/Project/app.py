from flask import Flask, render_template, request
from signin import *
from insert_daily_milk_production import *
from retrieve_daily_milk_production import *
from delete_daily_milk_production import *
from datetime import datetime
from edit_daily_milk_production import *
from insert_cow_records import *

app = Flask(__name__)
app.secret_key = 'emma'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/daily_milk_production.html')
def daily_milk_production():
    return render_template('daily_milk_production.html')

@app.route('/signin_form', methods = ['Post', 'Get'])
def signin():
    return signin_account()

@app.route('/mlkpro_form', methods = ['POST', 'Get'])
def mlkpro():
    return insert_milk_production()

@app.route('/search', methods=['GET','POST'])
def search():
    return milk_production()

@app.route('/delete/<string:date>/<int:id>', methods=['GET', 'POST'])
def delete(date, id):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    return delete_milk_production(date_obj, id)


@app.route('/cow_records.html')
def cow_records():
    return render_template('cow_records.html')

@app.route('/cowreco_form', methods = ['POST', 'Get'])
def cowreco():
    return insert_cow_records()

@app.route('/search_cowreco', methods=['GET','POST'])
def search_cow():
    if request.method == 'POST':
        type = request.form.get('search_bar')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CowRecords WHERE animalType = ?", (type, ))
        cow_data = cursor.fetchall()
        return render_template('cow_records.html', cow_data=cow_data)
    
@app.route('/c_delete/<int:animalID>', methods=['GET', 'POST'])
def delete_cr(animalID):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CowRecords WHERE animalID = ?", (animalID))
    cursor.execute("SELECT * FROM CowRecords WHERE animalID = ?", (animalID))
    cow_data = cursor.fetchall()
    conn.commit()
    return render_template('cow_records.html', cow_data=cow_data)

@app.route('/milk_sale.html')
def milk_sale():
    return render_template('milk_sale.html')

@app.route('/mlksale_form', methods = ['POST', 'GET'])
def insert_milk_sale():
    if request.method == 'POST':
        id = request.form.get('id')
        date = request.form.get('date')
        name = request.form.get('name')
        contact = request.form.get('contact')
        amntBought = request.form.get('amntBought')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MilkSale (clientId, date, name, contact, amountBought) VALUES (?, ?, ?, ?, ?)", (id, date, name, contact, amntBought))
        cursor.commit()
        cursor.close()
        return render_template('milk_sale.html')
    
@app.route('/search_mlk', methods=['GET','POST'])
def search_milksale():
    if request.method == 'POST':
        date = request.form.get('searchbar')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM MilkSale WHERE date = ?", (date, ))
        milksale_data = cursor.fetchall()
        return render_template('milk_sale.html', milksale_data=milksale_data)
    
@app.route('/delete_mlksale/<string:date>/<int:id>', methods=['GET', 'POST'])
def delete_milk_sale(date, id):
    date = datetime.strptime(date, '%Y-%m-%d')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MilkSale WHERE clientId = ? AND date = ?", (id, date))
    cursor.execute("SELECT * FROM MilkSale WHERE date = ?", (date, ))
    milksale_data = cursor.fetchall()
    conn.commit()
    return render_template('milk_sale.html', milksale_data=milksale_data)

@app.route('/farm_finance.html')
def farm_finance():
    return render_template('farm_finance.html')

@app.route('/daily_expenses_form', methods = ['POST', 'GET'])
def daily_expenses():
    if request.method == 'POST':
        date_incurred = request.form.get('date_incurred')
        exp_type = request.form.get('exp_type')
        exp_amnt = request.form.get('exp_amnt')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO DailyExpenses (dateIncurred, expensesType, expensesAmount) VALUES (?, ?, ?)", (date_incurred, exp_type, exp_amnt))
        cursor.commit()
        cursor.close()
        return render_template('farm_finance.html')
    
@app.route('/daily_income_form', methods = ['POST', 'GET'])
def daily_income():
    if request.method == 'POST':
        date_received = request.form.get('date_received')
        inc_type = request.form.get('inc_type')
        inc_amnt = request.form.get('inc_amnt')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO DailyIncome (dateReceived, incomeType, incomeAmount) VALUES (?, ?, ?)", (date_received, inc_type, inc_amnt))
        cursor.commit()
        cursor.close()
        return render_template('farm_finance.html')
    
@app.route('/search_finance', methods=['GET','POST'])
def search_finance():
    if request.method == 'POST':
        date = request.form.get('fi_srch')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DailyExpenses WHERE dateIncurred = ?", (date, ))
        d_exp_data = cursor.fetchall()
        cursor.execute("SELECT * FROM DailyIncome WHERE dateReceived = ?", (date, ))
        d_inc_data = cursor.fetchall()
        return render_template('farm_finance.html', d_exp_data=d_exp_data, d_inc_data = d_inc_data)
    
@app.route('/exp_delete/<string:dateIncurred>/<string:expensesType>', methods=['GET', 'POST'])
def delete_exp(dateIncurred, expensesType):
    dateIncurred = datetime.strptime(dateIncurred, '%Y-%m-%d')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DailyExpenses WHERE dateIncurred = ? AND expensesType = ?", (dateIncurred, expensesType, ))
    conn.commit()
    cursor.execute("SELECT * FROM DailyExpenses WHERE dateIncurred = ?", (dateIncurred, ))
    d_exp_data = cursor.fetchall()
    cursor.execute("SELECT * FROM DailyIncome WHERE dateReceived = ?", (dateIncurred, ))
    d_inc_data = cursor.fetchall()
    return render_template('farm_finance.html', d_exp_data=d_exp_data, d_inc_data = d_inc_data)

@app.route('/inc_delete/<string:dateReceived>/<string:incomeType>', methods=['GET', 'POST'])
def delete_inc(dateReceived, incomeType):
    dateReceived = datetime.strptime(dateReceived, '%Y-%m-%d')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DailyIncome WHERE dateReceived = ? AND incomeType = ?", (dateReceived, incomeType, ))
    conn.commit()
    cursor.execute("SELECT * FROM DailyIncome WHERE dateReceived = ?", (dateReceived, ))
    d_inc_data = cursor.fetchall()
    cursor.execute("SELECT * FROM DailyExpenses WHERE dateIncurred = ?", (dateReceived ))
    d_exp_data = cursor.fetchall()
    return render_template('farm_finance.html', d_exp_data=d_exp_data, d_inc_data = d_inc_data)

@app.route('/employees_list.html')
def employees_list():
    return render_template('employees_list.html')

@app.route('/emplist_form', methods = ['POST', 'Get'])
def emplist():
    if request.method == 'POST':
        employee_id = request.form.get('e_id')
        name = request.form.get('name')
        salary = request.form.get('salary')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Employees (employeeID, employeeName, salary) VALUES (?, ?, ?)", (employee_id, name, salary))
        cursor.commit()
        cursor.close()
        return render_template('employees_list.html')
    
@app.route('/search_emp', methods=['GET','POST'])
def search_emp():
    if request.method == 'POST':
        name = request.form.get('srch')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees WHERE employeeName = ?", (name, ))
        emp_data = cursor.fetchall()
        return render_template('employees_list.html', emp_data=emp_data)
    
@app.route('/emp_delete/<int:employeeID>', methods=['GET', 'POST'])
def delete_emp(employeeID):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employees WHERE employeeID = ?", (employeeID))
    cursor.execute("SELECT * FROM Employees WHERE employeeID = ?", (employeeID))
    emp_data = cursor.fetchall()
    conn.commit()
    return render_template('employees_list.html', emp_data=emp_data)

@app.route('/up_emplist', methods = ['POST', 'Get'])
def update_salary():
    if request.method == 'POST':
        emp_id = request.form.get('e_id')
        salary = request.form.get('up_salary')

        cursor = conn.cursor()
        cursor.execute("UPDATE Employees SET salary=? WHERE employeeID=?", (salary, emp_id))
        cursor.execute("SELECT * FROM Employees WHERE employeeID = ?", (emp_id))
        emp_data = cursor.fetchall()
        conn.commit()
    return render_template('employees_list.html', emp_data = emp_data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)