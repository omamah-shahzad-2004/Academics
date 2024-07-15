import pyodbc

def db_conn():
    conx_string = "DRIVER={SQL SERVER}; server=DESKTOP-AVT755B\\SQLEXPRESS; database=DFMS; trusted_connection=YES;"
    conn = pyodbc.connect(conx_string)
    return conn