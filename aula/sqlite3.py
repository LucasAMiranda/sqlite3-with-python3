import sqlite3

conn = sqlite3.connect('c:\python_sqlite3\example.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTIS EMPLOYEE")

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = '''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   ID INT(20) PRIMARY KEY NOT NULL,
   SEX CHAR(1),
   INCOME FLOAT
)'''

cursor.execute(sql)

conn.commit()
conn.close()
