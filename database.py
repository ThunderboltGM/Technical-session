import sqlite3
conn = sqlite3.connect('piet_Data_base.db')
tableCreationQuerry = '''create table student(name varchar(50),password int)'''
cur = conn.cursor()
cur.execute(tableCreationQuerry)
print("database created successfully")
cur.close()
conn.close()