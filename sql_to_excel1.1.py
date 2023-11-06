import sqlite3
from openpyxl import *

db_file = "northwind.db"
conn = sqlite3.connect("northwind.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Customers ORDER BY Country ")
data = cursor.fetchall()

workbook = Workbook()
woorksheet = workbook.active
woorksheet.title = "Data"

for row in data:
    woorksheet.append(row)
    
excel_file = "Ejercicios.xlsx"
workbook.save(excel_file)


